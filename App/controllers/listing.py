from App.models import User, Game, Listing
from App.database import db


def list_game(userId, gameId):
    user = User.query.get(userId)
    game = Game.query.get(gameId)
    if user and game:
        newlisting = Listing(userId, gameId)
        db.session.add(newlisting)
        db.session.commit()
        return True
    return False

def get_user_listings(user):
    return user.listings