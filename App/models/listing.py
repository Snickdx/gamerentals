from App.database import db
from datetime import datetime

class Listing(db.Model):
    listingId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    gameId = db.Column(db.Integer, db.ForeignKey('game.gameId'))
    condition = db.Column(db.String)
    price = db.Column(db.Float)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, userId, gameId, condition="good", price=10.40):
        self.userId = userId
        self.gameId = gameId
        self.condition = condition
        self.price = price

    def __repr__(self):
        return f'<listing {self.listingId} - {self.game.title} - {self.user.username}>'

    def toDict(self):
        return{
            'title': self.game.title,
            'condition': self.condition,
            'price': self.price,
            'created': self.created.strftime("%Y/%m/%d, %H:%M:%S")
        }

