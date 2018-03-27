"""Database model"""

from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

class Disaster(db.Model):
    """
    Disaster table database model
    """
    id = db.Column(db.Integer, primary_key=True)
    disasterNumber = db.Column(db.Integer, nullable=True)
    ihProgramDeclared = db.Column(db.Boolean, nullable=True)
    iaProgramDeclared = db.Column(db.Boolean, nullable=True)
    paProgramDeclared = db.Column(db.Boolean, nullable=True)
    hmProgramDeclared = db.Column(db.Boolean, nullable=True)
    state = db.Column(db.String(2), nullable=True)
    declarationDate = db.Column(db.DateTime, nullable=True)
    fyDeclared = db.Column(db.Integer, nullable=True)
    disasterType = db.Column(db.String(2), nullable=True)
    incidentType = db.Column(db.String(80), nullable=True)
    title = db.Column(db.String(120), nullable=True)
    incidentBeginDate = db.Column(db.DateTime, nullable=True)
    incidentEndDate = db.Column(db.DateTime, nullable=True)
    disasterCloseOutDate = db.Column(db.DateTime, nullable=True)
    declaredCountyArea = db.Column(db.String(80), nullable=True)
    placeCode = db.Column(db.Integer, nullable=True)
    hash_ = db.Column(db.String(80), nullable=True)
    lastRefresh = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return "{}".format(self.state)

# Create db schema with Command line interface (cli)
@app.cli.command()
def initdb():
    db.create_all()

@app.cli.command()
def parser():
    with open('misc/DisasterDeclarationsSummaries.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        counter = 0

        for row in reader:
            disaster = Disaster()
            disaster.disasterNumber = make_intger(row.get('disasterNumber'))
            disaster.ihProgramDeclared = make_boolean(row.get('ihProgramDeclared'))
            disaster.iaProgramDeclared = make_boolean(row.get('iaProgramDeclared'))
            disaster.paProgramDeclared = make_boolean(row.get('paProgramDeclared'))
            disaster.hmProgramDeclared = make_boolean(row.get('hmProgramDeclared'))
            disaster.state = make_string(row.get('state'))
            disaster.declarationDate = make_datetime(row.get('declarationDate'))
            disaster.fyDeclared = make_intger(row.get('fyDeclared'))
            disaster.disasterType = make_string(row.get('disasterType'))
            disaster.incidentType = make_string(row.get('incidentType'))
            disaster.title = make_string(row.get('title'))
            disaster.incidentBeginDate = make_datetime(row.get('incidentBeginDate'))
            disaster.incidentEndDate = make_datetime(row.get('incidentEndDate'))
            disaster.disasterCloseOutDate = make_datetime(row.get('disasterCloseOutDate'))
            disaster.declaredCountyArea = make_string(row.get('declaredCountyArea'))
            disaster.placeCode = make_intger(row.get('placeCode', None))
            disaster.hash_ = make_string(row.get('hash'))
            disaster.lastRefresh = make_datetime(row.get('lastRefresh'))

            db.session.add(disaster)
            db.session.commit()

            counter += 1
            print 'Inserted {} items'.format(counter)


# Helper functions
def make_string(value):
    """
    Takes the string argument and return string. If no then return None
    """
    try:
        if value:
            return str(value)
    except ValueError:
            return None


def make_intger(value):
    """
    Take the string value and return the integer value
    """
    try:
        if value:
            return int(value)
    except ValueError:
            return None


def make_boolean(value):
    """
    Take the string and return the boolean based on the int
    """
    try:
        if value == '1':
            return True
    except ValueError:
        return False


def make_datetime(value):
    """
    Take the string format of date and return the correct one
    """
    try:
        if value:
            return value
    except ValueError:
        return None

