#-*-coding:utf-8-*-

from . import services_blueprint
from flask import render_template

@services_blueprint.route("/")
def services_index():
    return render_template("services.html")