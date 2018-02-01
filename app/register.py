from app.auth import auth
from app.api.expenses import expenses
from app.api.categories import categories


def register_blueprints(app):
    app.register_blueprint(auth)
    app.register_blueprint(expenses)
    app.register_blueprint(categories)
