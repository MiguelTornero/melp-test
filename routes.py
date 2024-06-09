from flask import Blueprint

from views import get_all_restaurants, get_restaurant_by_id

bp = Blueprint("routes", __name__)

bp.add_url_rule("/restaurant", view_func=get_all_restaurants, methods=["GET"])
bp.add_url_rule("/restaurant/<id>", view_func=get_restaurant_by_id, methods=["GET"])