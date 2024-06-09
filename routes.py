from flask import Blueprint

from views import get_all_restaurants, get_restaurant_by_id, update_restaurant_by_id, delete_restaurant_by_id, create_restaurant, get_statistics_in_radius
bp = Blueprint("routes", __name__)

bp.add_url_rule("/restaurant", view_func=get_all_restaurants, methods=["GET"])
bp.add_url_rule("/restaurant/<id>", view_func=get_restaurant_by_id, methods=["GET"])
bp.add_url_rule("/restaurant/<id>", view_func=update_restaurant_by_id, methods=["PATCH"])
bp.add_url_rule("/restaurant/<id>", view_func=delete_restaurant_by_id, methods=["DELETE"])
bp.add_url_rule("/restaurant", view_func=create_restaurant, methods=["POST"])
bp.add_url_rule("/restaurants/statistics", view_func=get_statistics_in_radius, methods=["GET"])