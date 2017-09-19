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
    #邮件配置
    MAIL_SERVER="smtp-mail.outlook.com"
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME="pythonscientists@outlook.com"
    MAIL_PASSWORD="Linhanqiu1123."
    #邮件头配置
    LOCALNAME="PythonScientistsCompanion(PSC)"
    MAIL_SENDER="pythonscientists@outlook.com"