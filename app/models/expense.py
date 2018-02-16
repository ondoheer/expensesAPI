from app.models import db
from app.utils import utcnow
from app.utils import Serializer




class Expense(db.Model, Serializer):

    """
    Expense object.
    """

    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(255), nullable=False)
    date = db.Column(db.DateTime(timezone=True), server_default=utcnow(), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    month_id = db.Column(db.Integer, db.ForeignKey('months.year_month_usr'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category',
                               backref=db.backref('expenses', lazy='joined'))




    def __init__(self, name="", amount="", user_id="", category_id="", month_id=""):
        self.name = name
        self.amount = amount
        self.category_id = category_id,
        self.user_id = user_id,
        self.month_id = month_id


    def serialize(self):
        d = Serializer.serialize(self)
        del d['category']
        del d['user']
        del d['month']
        d['date'] = d['date'].strftime('%d/%m/%Y')
        return d

