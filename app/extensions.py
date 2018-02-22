from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.models import db

bcrypt = Bcrypt()
jwt = JWTManager()
cors = CORS()


def init_extensions(app):

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    # cors.init_app(app)
