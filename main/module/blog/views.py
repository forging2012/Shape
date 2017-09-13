#-*-coding:utf-8-*-

from . import blog_blueprint
from flask import render_template

@blog_blueprint.route("/")
def blog_index():
    return render_template("blog.html")