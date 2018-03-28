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
    $ export SQLALCHEMY_DATABASE_URI=
    $ export MAPBOX_ACCESS_TOKEN=

## Developer Usage

    pipenv install

    pipenv run flask initdb

    pipenv run flask parser

    pipenv run flask run
