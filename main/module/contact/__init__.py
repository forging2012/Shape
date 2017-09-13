#-*-coding:utf-8-*-

from flask import Blueprint

contact_blueprint = Blueprint(
    'contact',
    __name__,
    url_prefix = "/contact"
)

from . import views
