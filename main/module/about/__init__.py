#-*-coding:utf-8-*-

from flask import Blueprint

about_blueprint = Blueprint(
    'about',
    __name__,
    url_prefix = "/about"
)

from . import views
