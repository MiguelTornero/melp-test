from flask import Blueprint

bp = Blueprint("routes", __name__)

@bp.route("/")
def hello_world():
    return "hello, world"