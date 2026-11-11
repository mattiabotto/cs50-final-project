# CS50 Final Project

This is my final project for CS50 course: a personal website with a CMS (Content Management System) written with Flask,
for managin the content of the website.

## Project description

A flask application allows to manage the content of the website, following this workflow:

- Content is saved into a SQLite database, in the /database folder
- app.py is the main application, that allows to access the website from the route /admin: a UI with the same layout as
  the website, that allows to modify certain fields that are in the database.
- When the Save button is pressed, the database is updated and the page file into the folder /output_website is updated

## State of the project

The project is currently at his first stage of development (see below 'Good outcome'):

- The application is designed to run locally and to save the output locally
- The updated files of the website have to be manually pushed to deployment
- The UI is a basic one and has space for improvements
- No authentication is set for editing (pure local editing, but anyway the push requires git authentication)
- Which fields needs to be edited requires manual update of the database and the templates

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
This reboot time is thus only reduced to the few moments when an admin want to change the content.
The CMS could even run locally on a computer, or on PythonAnywhere or Fly.io

## Skills/knowledge to aquire or to expand

- **Python File Handling**: static web pages will be needed to be written using the Python application.
  Probable workflow will be: input content from a form -> elaboration of the data with Python ->
  Saving it into a database -> Writing a new static file -> Updating the file and publish it
- **Automatic git workflow with Python**: ideally the new files generated should be automatically pushed to a
  github repository (there are some modules like subprocess or GitPython for it),
  in order to not have to manually update the files
- **SSH authentication**: a better understanding of how public-key cryptography works when pushing a commit to GitHub
  through SSH
- **Usage of Python's subprocess module**: it allows to spawn new processes, for calling automatic git commit
  and pushes from python code

## Good, better and best outcomes

This project will be broken down into layered outcomes, in order to divide the difficulty.
A good outcome is an initial MVP (minimum viable product), to prove that the idea can work;
the better outcome and best outcome are improvements on the MVP

### Good outcome (MVP)

- A local Flask application connected to an SQLite database
- An /admin page allows to edit the content of the website and saves it locally on the computer
- No automatic publishing of the new content (it has to be pushed manually)
- Static fields editing

### Better outcome

- Automated Git Workflow to automatically publish the content on Save
- Authentication and Flask session
- Possibility of editing also dynamic lists or sections

### Best outcome

- Image uploads
- Live preview of changes before saving
- Sync status indicator ('Last synced at 2.15 PM')

## Use of external AI tools and workflow

Gemini AI on free-tier was used, mainly for:

- Brainstorming: putting together ideas, searching technical solutions between the many available online,
  searching resources for learning new skills and technologies to use.
- Coding: the code was written manually by the author, AI was used only for suggesting code that required new
  knowledge to be acquired.

## Git setting for automatic workflow
