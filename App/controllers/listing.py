from App.models import User, Game, Listing
from App.database import db

def get_user_listings(user):
    return user.listings

# creates a listing for a user
def list_game(userId, gameId, condition="good", price=10.00):
    user = User.query.get(userId)
    game = Game.query.get(gameId)
    if user and game:
        newlisting = Listing(userId, gameId, condition, price)
        db.session.add(newlisting)
        db.session.commit()
        return True
    return False

def delist_game(listingId, userId):
    listing = Listing.query.filter_by(listingId=listingId, userId=userId).first()
    if listing :
        db.session.delete(listing)
        db.session.commit()
        return True
    return False

def get_all_listings():
    return Listing.query.all()