from cs50 import SQL
from flask import Flask, redirect, render_template, request, url_for, send_from_directory
from helpers import get_content, normalize_content, write_page
from markupsafe import escape
import os

app = Flask(__name__)

db = SQL('sqlite:///database/mattiabtech.db')

@app.route('/')
def index():
    return redirect('/admin/home')


@app.route('/admin/')
def home():
    return redirect('/admin/home')


@app.route('/admin/projects')
def admin_projects():
    page = 'projects'

    # Editing a project will be another route ('/admin/projects/<int:id>/edit)
    # Deleting will popup a modal with 'are you sure' (Add to a list of projects to delete that is sent back and processed
    # only when the Save button is pressed, or add another route and redirect?)

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
        content = get_content(page, db)

        write_page(page, content=content)

        return redirect(url_for('admin', page=page))

    # Get regular content of the page
    content = db.execute(
        "SELECT * FROM content WHERE page_name = ?", page
    )

    # Get card content
    projects = db.execute(
        "SELECT * FROM projects"
    )

    return render_template('admin.html', content=content, projects=projects, title=page)

@app.route('/admin/projects/add', methods=['GET', 'POST'])
def add_project():

    if request.method == 'POST':

        # Insert into database new card
        db.execute(
            "INSERT INTO projects (title, content, img, repo_link, preview_link) VALUES (?, ?, ?, ?, ?)",
            request.form.get('title'), request.form.get('content'), request.form.get('img'),
            request.form.get('repo_link'), request.form.get('preview_link')
        )

        return redirect(url_for('admin_projects'))

    return render_template('add_project.html')

# TODO: edit route

@app.route('/admin/projects/<int:id>/delete', methods=['POST'])
def delete_project(id):

    page = 'projects'

    # Delete from database the project
    db.execute(
        "DELETE FROM projects WHERE id = ?", id
    )

    # Get generic content for the page
    content = get_content(page, db)

    # Get card-specific content from projects table
    projects = db.execute(
        "SELECT * FROM projects"
    )
    
    # Write updated page to output directory
    write_page(page, content=content, projects=projects)

    # Redirect to admin/projects
    return redirect(url_for('admin_projects'))


# Generic route, important that stays after the specific page routes, 
# otherwise this generic route will execute in place of the specific
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
        content = get_content(page, db)

        # Write the updated page to output directory
        write_page(page, content=content)

        return redirect(url_for('admin', page=page))

    content = db.execute(
        "SELECT * FROM content WHERE page_name = ?", page
    )
    return render_template('admin.html', content=content, title=page)


@app.route('/output_website/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('output_website/img', filename)