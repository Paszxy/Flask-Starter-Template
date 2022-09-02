from sqlalchemy.orm import backref
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Roles(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(100), unique=True)

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(128))
    roles_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def get_id(self):
           return (self.user_id)

