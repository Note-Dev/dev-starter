"""Main Application File"""
import os
import sys

sys.path.append("..")
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from urls import auth_blueprint

# EB looks for an 'application' callable by default.
application = app = Flask(__name__)
CORS(application)
application.config.from_object("config_app.DevelopmentConfig")
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
bcrypt = Bcrypt(application)
db = SQLAlchemy(application)
application.register_blueprint(auth_blueprint)

from backend.models.base_models import *
from backend.models.user import *


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    # application.debug = True
    application.run()
