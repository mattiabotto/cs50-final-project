from cs50 import SQL
from flask import flash, render_template
import subprocess
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

def get_content(page, db):
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


def run_git_push(commit_message):
    """
    Execute the normal git workflow 'add, commit, push', catching if some errors appear along the way.
    Success or failure message are sent to the templates with the flash function.
    """

    PUSH_TIMEOUT = 45

    try:
        subprocess.run(
            ['git', 'add', './docs'],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True,
            text=True
        )

        subprocess.run(
            ['git', 'commit', '-m', commit_message],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True,
            text=True
        )

        subprocess.run(
            ['git', 'push'],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=PUSH_TIMEOUT
        )

        flash(
            {
                'text': 'Updates correctly pushed to deploy!',
                'origin': 'run_git_push'
            },
            'success'
        )

    except subprocess.CalledProcessError as e:
        flash(
            {
                'text': f'Publish error: {e.stderr.strip()}',
                'origin': 'run_git_push'
            },
            'danger'
        )
    
    except subprocess.TimeoutExpired:
        flash(
            {
                'text': 'Publish timed out. Check your connection.',
                'origin': 'run_git_push'
            },
            'warning'
        )


def split_para(content):
    """Split the content into a list of strings, only when is_multipara flag is true (1)"""

    for field in content:
        if content[field]['is_multipara']:
            content[field]['content'] = content[field]['content'].split('\n\n')

    return content

def write_page(page, **kwargs):
    """
    Write a page on the disk, in the OUT_DIR specified. Accept a variable amount of kwargs as content 
    fetched from a database. 
    """
    
    # Create the output directory in case it doesn't exists
    OUT_DIR = 'docs'
    os.makedirs(OUT_DIR, exist_ok=True)

    filename = 'index.html' if page == 'home' else f'{page}.html'
    filepath = os.path.join(OUT_DIR, filename)

    # Write content to a new file, overriding the previous one in case
    with open(filepath, 'w') as f:
        f.write(render_template(filename, **kwargs))

    flash(
        {
            'text': 'Content saved locally, go to the Publish page to deploy it',
            'origin': 'write_page'
        },
        'success'
    )