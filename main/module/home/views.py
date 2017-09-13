#-*-coding:utf-8-*-

from . import home_blueprint
from flask import render_template

@home_blueprint.route("/")
def home_index():
    return render_template("index.html")