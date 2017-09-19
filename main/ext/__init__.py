#-*-coding:utf-8-*-
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()

from flask_mail import Mail
mail=Mail()

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view="auth.login_index"
login_manager.session_protection="strong"
login_manager.login_message="登录以获得更多功能"
login_manager.login_message_category="info"
