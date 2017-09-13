#-*-coding:utf-8-*-

from . import work_blueprint
from flask import render_template

@work_blueprint.route("/")
def work_index():
    return render_template("work.html")