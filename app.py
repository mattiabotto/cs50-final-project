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
    Get content of a page from the database, in the format of a dictionary, with content_name cols as keys and
    content as values. Ex:

    { 
        'title': 'Amazing Title',
        'biography': 'Amazing biography' 
    }
    """

    # List of dictionaries with db rows
    rows = db.execute(
        "SELECT * FROM content WHERE page_name = ?", page
    )

    return {row['content_name']: row['content'] for row in rows}