#-*-coding:utf-8-*-
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

"""
建立数据模型
"""
class User(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self,username):
        self.username = username

    def __repr__(self):
        return "<User %s>".format(self.username)