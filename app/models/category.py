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
