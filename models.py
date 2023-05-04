from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
class Coffee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    openTime = db.Column(db.String(100), nullable=False)
    closeTime = db.Column(db.String(100), nullable=False)
    coffee = db.Column(db.String(100), nullable=False)
    wifi = db.Column(db.String(100), nullable=False)
    power = db.Column(db.String(100), nullable=False)
    # submit = SubmitField(label='Submit')