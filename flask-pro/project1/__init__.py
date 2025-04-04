# _*_coding:utf-8 _*_


from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
import  logging
import os

from .bp.index import index
from .config import Config


db =  SQLAlchemy()
def registerLogging(app):
    app.logger.setLevel(logging.INFO) 
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
    file_handler = logging.FileHandler(os.path.join(os.getcwd(), 'project1/logs/flask-auto.log'),encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)



def registerBluepoint(app):
    from .bp.user import user_blueprint
    from .bp.admin import admin_blueprint
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)



def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    registerLogging(app=app)
    db.init_app(app=app)
    registerBluepoint(app)
    app.add_url_rule("/index", "index", index)



    return app