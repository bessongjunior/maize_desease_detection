import os

from flask import Flask, render_template
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
# from quart import render_template


# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object('app.config.Config')

db = SQLAlchemy(app) # flask-sqlalchemy
bc = Bcrypt(app) # flask-bcrypt

lm = LoginManager() # flask-loginmanager
lm.init_app(app)       # init the login manager

# Setup database
@app.before_request
def initialize_database():
    db.create_all()


# error handlers

@app.errorhandler(403)
def forbidden_page(error):
    return render_template("403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("500.html"), 500

# Import routing, models and Start the App
from app import routes, models 
