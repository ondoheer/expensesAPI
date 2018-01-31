from flask_bcrypt import Bcrypt
from flask_jwt_simple import JWTManager
from app.models import db

bcrypt = Bcrypt()
jwt = JWTManager()


def init_extensions(app):

	db.init_app(app)
	bcrypt.init_app(app)
	jwt.init_app(app)

