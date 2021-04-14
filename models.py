import datetime
db = SQLAlchemy(app)

class Fines(db.Model):

    __tablename__ = 'fines'

    id = db.Column(db.Integer, primary_key=True)
    offender_id = db.Column(db.Integer, nullable=False)
    prosecutor_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1500))
    cost = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(16), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    
class Gendarmes(db.Model):

    __tablename__ = 'gendarmes'

    id = db.Column(db.Integer, primary_key=True)
    chief = db.Column(db.Boolean, nullable=False, default=False)
    score = db.Column(db.Integer)
    
class Citizens(db.Model):

    __tablename__ = 'citizens'

    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.String(16), nullable=False)
    district = db.Column(db.Integer, nullable=False)
    
class Districts(db.Model):

    __tablename__ = 'districts'

    id = db.Column(db.Integer, primary_key=True)
    population = db.Column(db.Integer)
