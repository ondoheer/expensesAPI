from flask import Flask

from app.extensions import init_extensions
from app.register import register_blueprints


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

    return app

