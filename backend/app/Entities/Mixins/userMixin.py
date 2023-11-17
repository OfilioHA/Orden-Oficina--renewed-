from sqlalchemy.ext.declarative import declared_attr
from flask_praetorian import current_user_id
from extensions.alchemy import alchemy


class UserMixin (object):

    def __init__(self):
        self.created_by = current_user_id()

    @declared_attr
    def created_by(self):
        return alchemy.Column(alchemy.Integer, alchemy.ForeignKey('user.id'), nullable=False)

    @declared_attr
    def modified_by(self):
        return alchemy.Column(alchemy.Integer, alchemy.ForeignKey('user.id'))
