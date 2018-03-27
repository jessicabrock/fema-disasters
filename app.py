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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Database init
db = SQLAlchemy(app)


@app.route('/')
def index():
    """
    Main url for disaster app, returns the html file
    """
    mapbox_access_token = os.environ.get('MAPBOX_ACCESS_TOKEN')
    return render_template('base.html', mapbox_access_token=mapbox_access_token)


@app.route('/geo.json')
def geo_json():
    """
    Api interface for the Disaster App
    """
    fyDeclared = request.args.get('fyDeclared')
    incidentType = request.args.get('incidentType')

    # The GET args came from the js so it's should be null if not present,
    # We need to return None for python
    if fyDeclared == 'null':
        fyDeclared = None
    if incidentType == 'null':
        incidentType = None

    # Main query for this diaster api
    datas = Disaster.query.filter_by(fyDeclared=fyDeclared).filter_by(incidentType=incidentType).all()
    response = {
        "type": "FeatureCollection",
        "features": []
    }

    # Return empty response if the GET request doesn't contain any params
    length = len(datas)
    if length == 0:
        return jsonify(response)

    features = []
    for data in datas:
        state_feature = getattr(__import__('states'), data.state)
        features.append(state_feature)

    response['features'] = features
    return jsonify(response)
