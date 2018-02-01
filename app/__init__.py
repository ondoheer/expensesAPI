from flask import Flask, g
from flask_jwt_extended import get_jwt_identity

from app.extensions import init_extensions
from app.register import register_blueprints
from app.models.user import User


def create_app(app=None, config="DevelopmentConfig"):
    """
    creates a Flask App.
    :param app: Fask application instance
    :param config: object or location of the object to cofnigure the app
    :return: Flask app instance with extensions, blueprints, configs loaded
    """

    if not app:
        app = Flask(__name__)

    # config (has to happend before inits since some extensions
    # require this values)
    app.config.from_object("app.config.{}".format(config))


    ## inits
    init_extensions(app)

    # Blueprints
    register_blueprints(app)


    # @app.after_request
    # def add_user_to_global(response):
    #     """
    #     This is definetly the worst way to do this. It opens up so many vulnerabilities
    #     and keeps state, I'm getting rid of this so I keep aprsing the token on each request
    #     for the email
    #     """
    #     has_user_email = get_jwt_identity()
    #     if has_user_email:
    #         g.user = User.get_model_by_email(has_user_email)
    #     print("here we go: {}".format(g.user))
    #     return response


    return app

