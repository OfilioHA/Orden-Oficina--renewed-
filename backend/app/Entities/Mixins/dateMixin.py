from sqlalchemy.ext.declarative import declared_attr
from extensions.alchemy import alchemy
from datetime import date


class DateMixin (object):

    def __init__(self):
        self.created_at = date()

    @declared_attr
    def created_at(self):
        return alchemy.Column(alchemy.Date, nullable=False)

    @declared_attr
    def modified_at(self):
        return alchemy.Column(alchemy.Date, nullable=True)
