from app.auth import auth
from app.api.expenses import expenses


def register_blueprints(app):
    app.register_blueprint(auth)
    app.register_blueprint(expenses)
