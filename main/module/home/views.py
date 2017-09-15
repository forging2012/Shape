#-*-coding:utf-8-*-

from . import home_blueprint
from flask import render_template,send_file,make_response
import os

@home_blueprint.route("/")
def home_index():
    return render_template("index.html")

"""
下载简历
:param none
:return response
"""
@home_blueprint.route("/resume")
def home_resume():
    resume_route=os.path.join(os.getcwd(),r"file",r"linhanqiu.pdf")
    response = make_response(send_file(resume_route))
    response.headers["Content-Disposition"] = "attachment; filename=林韩秋的简历.pdf;"
    return response