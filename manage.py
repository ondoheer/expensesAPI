# manage.py


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app.models import db
from app.models.user import User
from app.models.expense import Expense
from app.models.category import Category



app = create_app()


manager = Manager(app)
migrate = Migrate(app, db)

# Migrations
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
        # add models
        User=User,
        Expense=Expense,
        Category=Category
    )
if __name__ == '__main__':
    manager.run()
