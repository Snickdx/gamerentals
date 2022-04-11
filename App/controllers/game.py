from App.models import Game
from App.database import db

def create_game(title, rating='Teen', platform='ps5', boxart='https://placecage.com/500/500', genre='action'):
    newgame = Game(title=title, rating=rating, platform=platform, boxart=boxart, genre=genre)
    db.session.add(newgame)
    db.session.commit()

def get_all_games(limit='all', offset=0):
    if limit == 'all':
        return Game.query.all()
    else :
        return Game.query.limit(limit).offset(offset).all()

def get_num_games():
    return Game.query.count()

def get_all_games_json(limit, offset):
    return [game.toDict() for game in get_all_games(limit, offset)]
