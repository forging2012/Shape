#-*-coding:utf-8-*-

class Config(object):
    pass
class DevConfig(Config):
    debug=True
    #数据库配置
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://linhanqiu:linhanqiu@localhost:3306/shape"
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    #wtf密钥
    SECRET_KEY="linhanqiu"