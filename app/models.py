from app import db
from datetime import datetime
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80)) # Title with max 80 characters 
    description = db.Column(db.Text, nullable=True) # Description allows null entry
    ingredients = db.Column(db.Text, nullable=True) # ingredients allows null entry
    instructions = db.Column(db.Text, nullable=True) #instructions allow null entry
    created = db.Column(db.DateTime, default=datetime.now) #gets the current date and time of submission

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    email = db.Column(db.String(32))
