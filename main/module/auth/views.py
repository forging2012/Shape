#-*-coding:utf-8-*-

from . import auth_blueprint
from flask import render_template

@auth_blueprint.route("/")
def login_index():
    return render_template("index.html")

@auth_blueprint.route("/")
def logout_index():
    return render_template("index.html")