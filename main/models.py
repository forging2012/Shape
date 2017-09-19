#-*-coding:utf-8-*-
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from main.ext import bcrypt
from flask_login import AnonymousUserMixin
from .ext import login_manager
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

"""
建立数据模型
"""
class User(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    confirmed = db.Column(db.Boolean,default=False)
    posts = db.relationship(
        "Post",
        backref = "user",
        lazy = "dynamic"
    )

    def __init__(self,username):
        self.username = username
    def __repr__(self):
        return "<User %s>".format(self.username)
    def set_password(self,password):
        self.password = bcrypt.generate_password_hash(password)
    def check_password(self,password):
        return bcrypt.check_password_hash(self.password,password)
    def is_authenticated(self):
        if isinstance(self,AnonymousUserMixin):
            return False
        else:
            return True
    def is_active(self):
        return True
    def is_anonymous(self):
        if isinstance(self,AnonymousUserMixin):
            return False
        else:
            return True
    def get_id(self):
        return self.id
    def gengerate_confirm(self,expiration=3600):
        s = Serializer(current_app.config["SECRET_KEY"],expiration)
        return s.dumps({"confirm":self.id})
    def confirm(self,token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get("confirm")!=self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
tags =  db.Table("post_tag",
                 db.Column("post_id",db.Integer,db.ForeignKey("post.id")),
                 db.Column("tag_id",db.Integer,db.ForeignKey("tag.id"))
                 )

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

class Post(db.Model):
    __tablename__="post"
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(255),index=True)
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    comments = db.relationship(
        "Comment",
        backref="post",
        lazy="dynamic"
    )
    user_id = db.Column(db.Integer(),db.ForeignKey("user.id"))
    tags = db.relationship("Tag",
                           secondary=tags,
                           backref=db.backref("posts",lazy="dynamic")
                           )

    def __init__(self,title):
        self.title = title

    def __repr__(self):
        return "<Post %s>".format(self.title)

class Comment(db.Model):
    __tablename__="comment"
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(),db.ForeignKey("post.id"))

    def __repr__(self):
        return "<Comment %s>".format(self.text[:15])

class Tag(db.Model):
    __tablename__="tag"
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(255),index=True)

    def __init__(self,title):
        self.title=title

    def __repr__(self):
        return "<Tag %s>".format(self.title)