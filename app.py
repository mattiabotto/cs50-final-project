from cs50 import SQL
from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

db = SQL('sqlite:///database/mattiabtech.db')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():

    # List of dictionaries with db rows
    rows = db.execute(
        "SELECT * FROM content WHERE page_name = ?", 'about'
    )

    # A dictionary of dictionaries, with content_name as key, id and content as values
    content = {}
    for row in rows:
        content[row['content_name']] = {
            'id': row['id'],
            'content': row['content']
        }
        

    return render_template('about.html', content=content)

@app.route('/admin/<page>', methods=['POST', 'GET'])
def admin(page):
    
    if request.method == 'POST':

        for content_name, content_value in request.form.items():
            db.execute(
                "UPDATE content SET content = ? "
                "WHERE page_name = ? AND content_name = ?",
                content_value, page, content_name
            )


    content = db.execute(
        "SELECT * FROM content WHERE page_name = ?", page
    )
    return render_template('admin.html', content=content)



def get_content(page):
    """
    Get content of a page from the database, in the format of a dictionary, with content_name cols as keys
    Values are dictionaries containing the id of the row and the content itself. Example:
    { 
        'title' : {
            'id': 1,
            'content': 'Amazing Title'
        },

        'biography': {
            'id': 2,
            'content': 'Amazing biography'
        }
    }
    """

    # List of dictionaries with db rows
    rows = db.execute(
        "SELECT * FROM content WHERE page_name = ?", page
    )

    # A dictionary of dictionaries, with content_name as key, id and content as values
    content = {}
    for row in rows:
        content[row['content_name']] = {
            'id': row['id'],
            'content': row['content']
        }

    return content


