from flask import Blueprint
from backend.views.basic_view import *

auth_blueprint = Blueprint("auth", __name__)

basic_view = BaseView.as_view("base_view")


auth_blueprint.add_url_rule("/", view_func=basic_view, methods=["GET"])
