#-*-coding:utf-8-*-

from . import about_blueprint
from flask import render_template

@about_blueprint.route("/")
def about_index():
    return render_template("about.html")