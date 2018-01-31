from app.auth import auth


def register_blueprints(app):
    app.register_blueprint(auth)
