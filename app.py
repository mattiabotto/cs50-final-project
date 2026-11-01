from cs50 import SQL
from flask import Flask, render_template

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