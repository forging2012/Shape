#-*-coding:utf-8-*-

from flask import Flask,redirect,url_for
# import blurprint
from main.module.home import home_blueprint
from main.module.about import about_blueprint
from main.module.contact import contact_blueprint
from main.module.services import services_blueprint
from main.module.work import work_blueprint
from main.module.blog import blog_blueprint
from main.module.auth import auth_blueprint
# import var
from main.models import db
# import ext
from main.ext import bcrypt
"""
:param object_name
:return app
"""
def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)
    #register blueprint
    app.register_blueprint(home_blueprint)
    app.register_blueprint(about_blueprint)
    app.register_blueprint(contact_blueprint)
    app.register_blueprint(services_blueprint)
    app.register_blueprint(work_blueprint)
    app.register_blueprint(blog_blueprint)
    app.register_blueprint(auth_blueprint)
    #instance
    db.init_app(app)
    bcrypt.init_app(app)
    @app.route("/")
    def index():
        return redirect(url_for("home.home_index"))
    return app