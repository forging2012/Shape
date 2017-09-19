#-*-coding:utf-8-*-
from flask_wtf import Form
from wtforms import StringField,SelectField,TextAreaField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,Email,Regexp,EqualTo
from main.models import User
from wtforms import ValidationError

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

    remeber = BooleanField("记住登录状态")

    submit = SubmitField("登录")
    def validate(self):
        check_validate = super(LoginForm,self).validate()

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
        if not user.check_password(self.password.data):
            self.username.errors.append(
                "错误的密码"
            )
            return False
        return True

class RegistrationForm(Form):
    email = StringField("邮件",validators=[DataRequired(),Length(max=255),Email()])
    username = StringField("用户名",validators=[DataRequired(),Length(max=255),
                                             Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
'Usernames must have only letters,'
'numbers, dots or underscores')])
    password = PasswordField("密码",validators=[DataRequired(),Length(1,255),EqualTo("password2",message="两次密码好像不符")])
    password2 = PasswordField("重复密码",validators=[DataRequired()])
    submit = SubmitField("注册用户")

    def validate_email(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("该邮箱已注册")
    def validate_usernme(self,field):
        if User.query.filter_by(usernmae = field.data).first():
            raise ValidationError("该用户名已注册")
class PostForm(Form):
    title = StringField("文章名称",[DataRequired(),Length(max=255)])
    text = TextAreaField("文章内容",[DataRequired(255)])
    publish_date = StringField("发表时间",[DataRequired(255)])
    comments = StringField("评论",[DataRequired(255)])
    user = StringField("作者",[DataRequired(255)])
    tag = StringField("标签",[DataRequired(255)])
    submit = SubmitField("完稿",[DataRequired(255)])
