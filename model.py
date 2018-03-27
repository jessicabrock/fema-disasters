"""Database model"""


from app import db


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
