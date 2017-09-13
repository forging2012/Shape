#-*-coding:utf-8-*-

from flask import Blueprint

home_blueprint = Blueprint(
    'home',
    __name__,
    url_prefix = "/home"
)

from . import views
