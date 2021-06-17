# Fema-Disaster application

Reads disaster data provided from FEMA through a cvs file. User can select the year and disaster type they are looking for and the results will displays on map, using the Mapbox API.

## App Info
    Name: Fema-Disaster app
    Version: 1.0
    Developer: Jessica Brock, jessicabrock03@gmail.com
    URL: https://disasterapp.herokuapp.com

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
