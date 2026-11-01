from cs50 import SQL
from flask import Flask, redirect, render_template, request, url_for
from markupsafe import escape
import os

app = Flask(__name__)

db = SQL('sqlite:///database/mattiabtech.db')

@app.route('/admin/')
def home():
    return redirect('/admin/home')

@app.route('/admin/<page>', methods=['POST', 'GET'])
def admin(page):

    page = escape(page)
    
    if request.method == 'POST':

        # Update database with form fields values
        for content_name, content_value in request.form.items():
            
            content_value = normalize_content(content_value)
            db.execute(
                "UPDATE content SET content = ? "
                "WHERE page_name = ? AND content_name = ?",
                content_value, page, content_name
            )

        # Get new content from database
        content = get_content(page)

        # Create the output directory in case it doesn't exists
        OUT_DIR = 'output_website'
        os.makedirs(OUT_DIR, exist_ok=True)

        filename = 'index.html' if page == 'home' else f'{page}.html'
        filepath = os.path.join(OUT_DIR, filename)

        # Write content to a new file, overriding the previous one in case
        with open(filepath, 'w') as f:
            f.write(render_template(filename, content=content))

        return redirect(url_for('admin', page=page))

    content = db.execute(
        "SELECT * FROM content WHERE page_name = ?", page
    )
    return render_template('admin.html', content=content)



def get_content(page):
    """
    Get content of a page from the database, in the format of a dictionary, with content_name as keys and
    a dictionary with content and is_multipara flag as keys.
    If is_multipara is set to 1, then the content value will be a list of strings, representing different paragraphs,
    when the input is separated by a double line

    { 
        'title': {'content': 'Amazing Title', 'is_multipara': 0}
        'biography': {'content': ['Amazing biography.', 'Another paragraph.], 'is_multipara': 1} 
    }
    """

    # List of dictionaries with db rows
    rows = db.execute(
        "SELECT * FROM content WHERE page_name = ?", page
    )

    content = {}

    for row in rows:
        content[row['content_name']] = {
            'content': row['content'],
            'is_multipara': row['is_multipara']
        }

    content = split_para(content)

    return content

def normalize_content(content):
    r"""Normalize a string of content, replacing Windows-style line endings \r\n with \n"""
    return content.replace('\r\n', '\n')

def split_para(content):
    """Split the content into a list of strings, only when is_multipara flag is true (1)"""

    for field in content:
        if content[field]['is_multipara']:
            content[field]['content'] = content[field]['content'].split('\n\n')

    return content