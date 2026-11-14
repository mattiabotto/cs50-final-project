# CS50 Final Project - Personal Website with a Flask-based Content Management System

This is my final project for CS50 course: a personal website with a CMS (Content Management System) written with Flask,
for managin the content of the website.

## Video Demo

URL to Video: (https://www.youtube.com/watch?v=IUeLUPvpJRo)

## Project description

A flask application allows to manage the content of the website, following this workflow:

- Content is saved into a SQLite database, in the /database folder
- app.py is the main application, that allows to access the website from the route /admin: a UI with the same layout as
  the website, that allows to modify certain fields that are in the database.
- When the Save button is pressed, the database is updated and the page file into the folder /output_website is updated
- A Publish page allows to commit and push the updated files to the GitHub repository, so that the website is automatically
  deployed with the new content
- Style is done mainly with Bootstrap, plus some custom CSS on top

## Initial idea and exploring

The initial idea is to create a CMS in Flask that can allow an admin of
a static-content website to change the content of it.
The website needs to be a simple-enough website that can be hosted anywhere for free on a CDN like
Github Pages, Cloudfare, Netlify, or similars, while the Flask application will take care of giving a GUI
for changing the content of the page and save new static files on 'Save'.
This means that the website will load very fast even on free-tier CDN: only static files will be served on requests,
the flask application runs only when the admin wants to change the content.
This can potentially solve the problem of running web-apps on free tier:
instances are shut-down after usually 15 minutes
of inactivities, causing a reboot time of 30-60 seconds for the next request
(it would cause the website to run very slow).
The Flask application for managing the content runs locally.

## Skills/knowledge to aquire or to expand

- **Python File Handling**: static web pages will be needed to be written using the Python application.
  Probable workflow will be: input content from a form -> elaboration of the data with Python ->
  Saving it into a database -> Writing a new static file -> Updating the file and publish it
- **Automatic git workflow with Python**: ideally the new files generated should be automatically pushed to a
  github repository (there are some modules like subprocess or GitPython for it),
  in order to not have to manually update the files
- **SSH authentication**: a better understanding of how public-key cryptography works when pushing a commit to GitHub
  through SSH and how to configure aliases for remotes in the .ssh/config file
- **Usage of Python's subprocess module**: it allows to spawn new processes, for calling automatic git commit
  and pushes from python code
- **Database updating from forms**: usage of a combination of client-side DOM manipulation with JavaScript and
  server-side database queries for updating fields, reordering cards, etc...

## Project Structure

Here is an overview of the key files and directories in the project and what they do:

```text
cs50-final-project/
│
├── database/                   # Database-related files (database itself is not pushed to GitHub, it is kept local)
│   ├── init_db.py              # Initialize the database with the schema in schema.sql (Attention, it erase an existing database)
│   └── schema.sql              # Schema for the database
│
├── docs/                       # Folder where the final output of the personal website is written
│   ├── img/
│   ├── style/
│   ├── about.html              # Those html files are pure html static files, not Jinja templates
│   ├── index.html
│   └── projects.html
│
├── static/
│   ├── style.css               # Global styling and layout rules
│   ├── reorder.js              # Client-side DOM manipulation for card swapping and visual effects
│   └── other static assets
│
├── templates/                  # Templates used for the flask app are marked with (admin)
│   ├── about.html              # Template for about page
│   ├── add_project.html        # Template for adding a project (admin)
│   ├── admin_layout.html       # Base layout for the flask application (admin)
│   ├── admin.html              # Template for the basic admin pages (admin)
│   ├── edit_project.html       # Template for editing a project (admin)
│   ├── index.html              # Template for homepage of the website
│   ├── layout.html             # Base template with common layout, navbar, and block structure
│   ├── projects.html           # Template for the projects page
│   ├── publish.html            # Template for the publish page (admin)
│   └── reorder_projects.html   # Template for changing the order of the projects (admin)
│
├── app.py                      # Main Flask application, with routes for each route
├── helpers.py                  # Helper functions (to get content from database, write an html output file and push to GitHub)
└── README.md                   # Project documentation
```

## Git setting for automatic workflow

- Pressing Save on the various edit pages only makes a specific html page to be updated and rewritten in the /docs folder.
- Pressing Publish in the Publish page triggers an automatic commit + push git workflow on only the /docs folder, where
  the output static html files are living.
- Push to GitHub is made with SSH, with another SSH key than the global key used for manual pushes. An alias set into the
  ~/.ssh/config file, mapping cs50_final to github.com, allows to use that specific key when pushing to this specific
  repository. The key is used in GitHub as a deploy key.

## Use of external AI tools

Gemini AI on free-tier was used, mainly for:

- Brainstorming: putting together ideas, searching technical solutions between the many available online,
  searching resources for learning new skills and technologies to use.
- Coding: the code was written manually by the author, AI was used only for suggesting code that required new
  knowledge to be acquired.
- No code was ever put blindly from AI without understanding what it does.
