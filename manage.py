#-*-coding:utf-8-*-
import os
from main import create_app
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from main.models import db,User

config = os.environ.get('shape_cfg','dev')
app = create_app('main.config.%sConfig'%config.capitalize())
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command("server",Server())
manager.add_command("db",MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User)

if __name__=="__main__":
    app.run(host="0.0.0.0")
    # manager.run()