from App.models import User, Game
from App.database import db


def list_game(userId, gameId):
    user = User.query.get(userId)
    game = Game.query.get(gameId)
    if user and game:
        user.listings.append(game)
        db.session.add(user)
        db.session.commit()
        return True
    return False

def get_user_listings(user):
    return user.listings