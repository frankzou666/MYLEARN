
from flask import g
from flask_sqlalchemy.model import Model
from flask import  current_app

from project1 import db

current_app.app_context()

class User(current_app.db.Model):
    __table__name="t_user"
    id = current_app.db.Column(current_app.db.Integer, primary_key=True)
    username = current_app.db.Column(current_app.db.String,(200))
    password = current_app.db.Column(current_app.db.String, (200))




