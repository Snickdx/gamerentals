from App.database import db
from datetime import datetime

class Rental(db.Model):
    rentalId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    listingId = db.Column(db.Integer, db.ForeignKey('listing.listingId'))
    rental_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime, default=None)

    def __init__(self, userId, listingId):
        self.userId = userId
        self.listingId = listingId
    
    def __repr__(self):
        return f'<rental {self.rentalId} >'