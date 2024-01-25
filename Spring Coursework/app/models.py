from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    picture = db.Column(db.String(100))
    price = db.Column(db.Integer)
    environmental_impact = db.Column(db.Float)
