#-*-coding:utf-8-*-
import os
from main import create_app

config = os.environ.get('shape_cfg','dev')
app = create_app('main.config.%sConfig'%config.capitalize())

if __name__=="__main__":
    app.run()