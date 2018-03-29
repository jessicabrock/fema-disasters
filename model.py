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


    def example_data():
        """Create some sample data for testing."""
        disaster1 = Disaster(id=1, disasterNumber=null,ihProgramDeclared=null,iaProgramDeclared=null,paProgramDeclared=null,hmProgramDeclared=null,state='California',declarationDate=null,fyDeclared=1998,disasterType='DR',incidentType='Tornado',title=null,incidentBeginDate=null,incidentEndDate=null,disasterCloseOutDate=null,declaredCountyArea=null,placeCode=null,hash_=null,lastRefresh=null)
        disaster2 = Disaster(id=2, disasterNumber=null,ihProgramDeclared=null,iaProgramDeclared=null,paProgramDeclared=null,hmProgramDeclared=null,state='California',declarationDate=null,fyDeclared=2004,disasterType='DR',incidentType='Flood',title=null,incidentBeginDate=null,incidentEndDate=null,disasterCloseOutDate=null,declaredCountyArea=null,placeCode=null,hash_=null,lastRefresh=null)
        disaster3 = Disaster(id=3, disasterNumber=null,ihProgramDeclared=null,iaProgramDeclared=null,paProgramDeclared=null,hmProgramDeclared=null,state='California',declarationDate=null,fyDeclared=1994,disasterType='DR',incidentType='Earthquake',title=null,incidentBeginDate=null,incidentEndDate=null,disasterCloseOutDate=null,declaredCountyArea=null,placeCode=null,hash_=null,lastRefresh=null)

        db.session.add_all([disaster1, disaster2, disaster3])
        db.session.commit()
