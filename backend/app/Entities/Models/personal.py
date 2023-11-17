from sqlalchemy_serializer import SerializerMixin
from extensions.alchemy import alchemy


class Personal(alchemy.Model, SerializerMixin):

    id = alchemy.Column(alchemy.Integer, primary_key=True)
    firstnames = alchemy.Column(alchemy.String, nullable=False)
    lastnames = alchemy.Column(alchemy.String, nullable=False)
    birthday = alchemy.Column(alchemy.String)
    active = alchemy.Column(alchemy.Boolean, default=True)

    serialize_rules = ()

    def __init__(self, firstname, lastname, birthday, gender_id, type_id):
        self.firstnames = firstname
        self.lastnames = lastname
        self.birthday = birthday
        self.gender_id = gender_id
        self.type_id = type_id
        self.active = True


