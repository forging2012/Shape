#-*-coding:utf-8-*-

from . import auth_blueprint
from flask import render_template,flash,redirect,url_for
from ...forms import LoginForm,RegistrationForm
from ...models import User
from flask_login import login_user,logout_user,current_user
from ...models import db
from ...utils import send_mail

@auth_blueprint.route("/login",methods=["GET","POST"])
def login_index():
    form = LoginForm()
    if form.validate_on_submit():
        username = User.query.filter_by(
            username=form.username.data
        ).first()
        login_user(username,remember=form.remeber.data)
        flash("您已经成功登录",category="success")
        return redirect(url_for("about.about_index"))
    return render_template("login.html",form=form)


@auth_blueprint.route("/logout",methods=["GET","POST"])
def logout_index():
    logout_user()
    flash("您已经成功退出系统",category="success")
    return render_template("index.html")

@auth_blueprint.route("/register",methods=["POST","GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.username.data)
        user.set_password(form.password.data)
        user.email = form.email.data
        db.session.add(user)
        db.session.commit()
        token = user.gengerate_confirm()
        send_mail.send_mail(user.email,"确认您的账户","auth/email/confirm",user=user,token=token)
        flash("一封确认邮件已发送到您的邮件，请注意查收")
        # flash("您已成功注册，现在可以登录.")
        return redirect(url_for("auth.login_index"))
    return render_template("auth/register.html", form=form)

@auth_blueprint.route("/confirm/<token>")
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for("home.home_index"))
    if current_user.confirm(token):
        flash("您已经确认您的账户，谢谢")
    else:
        flash("不好意思，这个确认链接已经失效")
    return redirect(url_for("home.home_index"))

# @auth_blueprint.before_app_request
# def before_request():
#     if  not current_user.is_authenticated \
#         and not current_user.confirmed:
#         return redirect(url_for('auth.unconfirmed'))
# @auth_blueprint.route('/unconfirmed')
# def unconfirmed():
#     if current_user.is_anonymous() or current_user.confirmed:
#         return redirect(url_for('home.home_index'))
#     return render_template('about.html')