# python modules
import os
import csv

# third-party modules
import geocoder
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, jsonify, request

# Flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')


@app.route('/')
def index():
    """
    Main url for disaster app, returns the html file
    """
    return render_template('base.html')
