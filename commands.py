import csv
from app import app, db
from models import Disaster


# Helper functions
def make_string(value):
    """
    Takes the string argument and return string.
    """
    if value:
        return str(value)
    return None


def make_intger(value):
    """
    Take the string value and return the integer value
    """
    if value:
        return int(value)
    return None


def make_boolean(value):
    """
    Take the string and return the boolean based on the integer
    """
    if value == '1':
        return True
    return False


def make_datetime(value):
    """
    Take the string format of date and return the correct one
    """
    if value:
        return value
    return None


# Create db schema with command line interface (cli)
@app.cli.command()
def initdb():
    """Disaster app database schema"""
    db.create_all()


@app.cli.command()
def parser():
    """Load data from csv file to db"""
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
