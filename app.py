from cs50 import SQL
from flask import Flask, redirect, render_template, request, url_for, send_from_directory
from helpers import get_content, normalize_content, write_page
from markupsafe import escape

app = Flask(__name__)

app.config.from_mapping(
        SECRET_KEY='dev'
)

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

    page = 'projects'

    if request.method == 'POST':

        # Insert into database new card
        db.execute(
            "INSERT INTO projects (title, content, img, repo_link, preview_link) VALUES (?, ?, ?, ?, ?)",
            request.form.get('title'), request.form.get('content'), request.form.get('img'),
            request.form.get('repo_link'), request.form.get('preview_link')
        )

        # Get generic content for the page
        content = get_content(page, db)
    
        # Get card-specific content from projects table
        projects = db.execute(
            "SELECT * FROM projects"
        )
        
        # Write updated page to output directory
        write_page(page, content=content, projects=projects)

        return redirect(url_for('admin_projects'))

    return render_template('add_project.html')


@app.route('/admin/projects/<int:id>/edit', methods=['GET', 'POST'])
def edit_projects(id):

    page = 'projects'

    if request.method == 'POST':

        # Update database with edited content
        db.execute(
            "UPDATE projects"
            " SET title = ?, content = ?, img = ?, repo_link = ?, preview_link = ?" 
            " WHERE id = ?",
            request.form.get('title'), request.form.get('content'), request.form.get('img'),
            request.form.get('repo_link'), request.form.get('preview_link'), id
        )

        # Get generic content for the page
        content = get_content(page, db)
    
        # Get card-specific content from projects table
        projects = db.execute(
            "SELECT * FROM projects"
        )
        
        # Write updated page to output directory
        write_page(page, content=content, projects=projects)
        
        return redirect(url_for('admin_projects'))

    # Get project's content
    project = db.execute(
        "SELECT * FROM projects WHERE id = ?", id
    )[0]

    return render_template('edit_project.html', project=project)


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


# Automatically push the content of docs to GitHub
@app.route('/admin/publish', methods=['POST', 'GET'])
def publish():


    return render_template('publish.html')


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


@app.route('/docs/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('docs/img', filename)


if __name__ == '__main__':
    app.run()