#-*-coding:utf-8-*-
from flask_wtf import Form
from wtforms import StringField,SelectField,TextAreaField,PasswordField
from wtforms.validators import DataRequired,Length
from main.models import User

class CommentForm(Form):
    name = StringField(
        "名字",
        validators=[DataRequired(),Length(max=255)]
    )
    text = TextAreaField(u"评论",validators=[DataRequired()])

class LoginForm(Form):
    username = StringField("姓名",
                         [DataRequired(),Length(max=255)])
    password = PasswordField("密码",[DataRequired()])

    def validate(self):
        check_validate = super(LoginForm,self.validate())

        #验证没通过
        if not check_validate:
            return False
        #检查是否存在拥有该用户名的用户
        user = User.query.filter_by(
            username = self.username.data
        ).first()
        if not user:
            self.username.errors.append(
                "未找到用户名"
            )
            return False
        #检查密码是否匹配
        if not self.user.check_password(self.password.data):
            self.username.errors.append(
                "错误的密码"
            )
            return False
        return True