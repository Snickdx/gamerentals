from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from urllib.parse import urlparse

from App.controllers import (
    get_all_games_json,
    get_num_games
)

game_views = Blueprint('game_views', __name__, template_folder='../templates')


@game_views.route('/api/games', methods=['GET'])
def get_user_page():
    limit = request.args.get('limit', default=50, type=int)
    offset = request.args.get('offset', default=0, type=int)
    num_games  = get_num_games()
    num_pages = num_games/limit
    page = int(offset/limit) + 1
    hostname = urlparse(request.base_url).hostname
    next = None if page > num_pages - 1 else f'https://{hostname}/api/games?limit{limit}&offset={offset+limit}'
    prev = None if page == 1 else f'https://{hostname}/api/games?limit{limit}&offset={offset-limit}'
    return jsonify(
        { 
            "list" : get_all_games_json(limit, offset), 
            "page": f'Showing page { page } of { int(num_pages) }',
            "prev" : prev,
            "next" : next
        }
    )