#-*-coding:utf-8-*-

from flask import Blueprint

work_blueprint = Blueprint(
    'work',
    __name__,
    url_prefix = "/work"
)

from . import views
