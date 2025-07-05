from app import db

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    category = db.Column(db.String(50))
    last_updated = db.Column(db.DateTime)
