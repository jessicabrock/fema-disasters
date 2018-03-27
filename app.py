# python modules
import os

# third-party modules
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, jsonify, request

# app modules
from model import Disaster

# Flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

# Database init
db = SQLAlchemy(app)


@app.route('/')
def index():
    """
    Main url for disaster app, returns the html file
    """
    return render_template('base.html')
