from app.models import db
from app.utils import Serializer
from app.models.category import Category
from collections import OrderedDict

from datetime import datetime


class MonthMixin(object):
    """
    Month model helper methods
    """
    @staticmethod
    def build_user_month_code(user_id):
        """
        builds current month user month code
        """
        date = datetime.now()
        year, month = date.year, date.month
        year_month_usr = "{}{}{}".format(
            year, month, user_id
        )
        return year_month_usr

    @property
    def total_expenses(self):
        return sum([expense.amount for expense in self.expenses])

    @property
    def month(self):
        user_len = len(str(self.user_id))
        code_len = len(str(self.year_month_usr))
        # year length this will work until the year 10000
        month_len = code_len - user_len - 4
        if month_len == 1:
            return int(str(self.year_month_usr)[4:5])
        else:
            return int(str(self.year_month_usr)[4:6])

    @property
    def year(self):
        return str(self.year_month_usr)[:4]

    def expenses_by_category(self):
        """
        return: dict of categories and amounts, suposed to be ordered
        but its not TODO
        """


        expenses_by_category = {}
        for expense in self.expenses:
            if expense.category not in expenses_by_category:
                
                expenses_by_category["{}".format(expense.category)] = {
                    'name': expense.category.name,
                    'label': expense.category.label,
                    'amount': expense.amount
                }
            else:
                current_amount = expenses_by_category["{}".format(
                    expense.category)]
                expenses_by_category["{}".format(
                    expense.category)] = {
                    'name': expense.category.name,
                    'label': expense.category.label,
                    'amount': current_amount + expense.amount
                }

        normalized_expenses_by_category = []

        # {
        #   '3': {
        #     amount: 23.5,
        #     label: 'Taxi',
        #     name: 'taxi'
        #   },
        for category in expenses_by_category.keys():
            new_dict = expenses_by_category[category]
            new_dict.update({"id":category})
            normalized_expenses_by_category.append(new_dict)
        return normalized_expenses_by_category


    def expenses_for_category(self, category_id):
        category = db.session.query(Category).get(category_id)
        return category.sum_expenses_by_month(self.id)

    @classmethod
    def get_last_n_months(cls, user_id, n):
        n_months = db.session.query(cls)\
            .filter(cls.user_id == user_id)\
            .order_by(cls.year_month_usr.desc()).limit(n)
        return n_months



class Month(db.Model, Serializer, MonthMixin):

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

    def serialize(self):
        d = Serializer.serialize(self)
        # del d['users']
        del d['expenses']
        return d
