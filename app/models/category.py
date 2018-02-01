from app.models import db
from app.utils import Serializer

class Category(db.Model, Serializer):

    """
    Category object.
    """

    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(50), nullable=False)
    label = db.Column(db.Unicode(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return self.name

    def __init__(self, label, user_id):
        self.user_id = user_id
        self.label = label
        self.name = label.lower().replace(" ", "-")


    def serialize(self):
        d = Serializer.serialize(self)
        del d['user']
        del d['expenses']
        return d




