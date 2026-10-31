# CS50 Final Project

This is my final project for CS50 course.

## Use of external AI tools and workflow

Gemini AI on free-tier was used, mainly for:

- Brainstorming: putting together ideas, searching technical solutions between the many available online,
  searching resources for learning new skills and technologies to use.
- Coding: the code was written manually by the author, AI was used only for suggesting code that required new
  knowledge to be acquired.

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

## Skills to aquire or to expand

- **Python File Handling**: static web pages will be needed to be written using the Python application.
  Probable workflow will be: input content from a form -> elaboration of the data with Python ->
  Saving it into a database -> Writing a new static file -> Updating the file and publish it
- **Automatic git workflow with Python**: ideally the new files generated should be automatically pushed to a
  github repository (there are some modules like subprocess or GitPython for it),
  in order to not have to manually update the files

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
