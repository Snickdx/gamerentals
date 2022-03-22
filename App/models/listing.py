from App.database import db
from datetime import datetime

listing = db.Table('listing', 
    db.Column('listingId', db.Integer, primary_key=True),
    db.Column('userId', db.Integer, db.ForeignKey('user.id')),
    db.Column('gameId', db.Integer, db.ForeignKey('game.gameId')),
    db.Column('condition', db.String),
    db.Column('price', db.Float),
    db.Column('created', db.DateTime, default=datetime.utcnow)       
)
