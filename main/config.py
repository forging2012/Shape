#-*-coding:utf-8-*-

class Config(object):
    pass
class DevConfig(Config):
    debug=True
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://linhanqiu:linhanqiu@localhost:3306/shape"
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_TRACK_MODIFICATIONS=True