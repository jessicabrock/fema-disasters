# Fema-Disaster application

## App Info
    Name: Fema-Disaster app
    Version: 1.0
    Developer: Jessica Brock, jessicabrock03@gmail.com
    URL:

## Installation

    $ pip install pipenv
    $ cd <project name>
    $ pipenv install
    $ pipenv shell
    $ export FLASK_APP=commands.py
    $ export FLASK_DEBUG=1
    $ export SQLALCHEMY_DATABASE_URI=<database URI>
    $ export MAPBOX_ACCESS_TOKEN=<mapbox api key>

## Local Server

    $ gunicorn commands:app

    You should see a url you can copy/paste into your web browser.
    Example, http://127.0.0.1:8000
