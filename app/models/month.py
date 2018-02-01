from app.models import db
from app.utils import Serializer


class Month(db.Model, Serializer):

    """
    acumulado de gastos mensuales
    """

    __tablename__ = "months"

    year_month_usr = db.Column(db.Integer, primary_key=True, autoincrement=False)


    expenses = db.relationship("Expense", backref='month', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, year_month_usr="", user_id=""):
        self.year_month_usr = year_month_usr
        self.user_id = user_id

    def __str__(self):
        return "{}-{}".format(
            str(self.year_month_usr)[:-1],
            str(self.year_month_usr)[-1]
        )
