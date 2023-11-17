from sqlalchemy.ext.declarative import declared_attr
from extensions.alchemy import alchemy
from datetime import datetime

class DateMixin (object):

    @declared_attr
    def created_at(self):
        return alchemy.Column(alchemy.String, default=datetime.now().strftime("%Y-%m-%d %H:%M"), nullable=False)

    @declared_attr
    def modified_at(self):
        return alchemy.Column(alchemy.String, nullable=True)
