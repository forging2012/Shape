#-*-coding:utf-8-*-

from flask import Blueprint

services_blueprint = Blueprint(
    'services',
    __name__,
    url_prefix = "/services"
)

from . import views
