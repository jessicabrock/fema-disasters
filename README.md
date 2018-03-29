# Fema-Disaster application

## App Info
    Name: Fema-Disaster app
    Version: 1.0
    Developer: Jessica Brock, jessicabrock03@gmail.com
    URL:

## Installation

    $ cd <project name>
    $ export CURRENT_YEAR=$(date +'%Y')
    $ export FLASK_APP=commands.py
    $ export FLASK_DEBUG=1
    $ export SQLALCHEMY_DATABASE_URI=
    $ export MAPBOX_ACCESS_TOKEN=

## Developer Usage

    $ pipenv install

    $ pipenv shell

    pipenv run flask initdb

    pipenv run flask parser

    pipenv run flask run
