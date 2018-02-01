from app.models import db
from app.extensions import bcrypt
from app.utils import Serializer
import datetime
from flask import current_app, jsonify


class User(db.Model, Serializer):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    expenses = db.relationship("Expense", backref='user', lazy='dynamic')
    categories = db.relationship("Category", backref='user', lazy="dynamic")


    def __init__(self, email, password, fullname, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password
        ).decode('utf-8')
        self.fullname = fullname
        self.admin = admin

    @staticmethod
    def validate_password(email, password):


        exists = db.session.query(User).filter_by(email=email).first()
        if exists is None:

            return False

        return bcrypt.check_password_hash(exists.password, password)


    @staticmethod
    def get_model_by_email(email):
        return db.session.query(User).filter_by(email=email).first()


    def serialize(self):
        d = Serializer.serialize(self)
        del d['password']
        del d['expenses']
        del d['categories']
        return d
