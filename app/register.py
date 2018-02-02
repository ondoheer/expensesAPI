from app.auth import auth
from app.api.expenses import expenses
from app.api.categories import categories
from app.api.main import main


def register_blueprints(app):
    app.register_blueprint(auth)
    app.register_blueprint(expenses)
    app.register_blueprint(categories)
    app.register_blueprint(main)
