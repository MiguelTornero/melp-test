from flask import Blueprint

from views import get_all_restaurants

bp = Blueprint("routes", __name__)

bp.add_url_rule("/restaurant", view_func=get_all_restaurants, methods=["GET"])
