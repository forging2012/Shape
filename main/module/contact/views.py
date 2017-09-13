#-*-coding:utf-8-*-

from . import contact_blueprint
from flask import render_template

@contact_blueprint.route("/")
def contact_index():
    return render_template("contact.html")