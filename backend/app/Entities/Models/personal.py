from sqlalchemy_serializer import SerializerMixin
from extensions.alchemy import alchemy
from .catalogs import Gender


class Personal(alchemy.Model, SerializerMixin):

    id = alchemy.Column(alchemy.Integer, primary_key=True)
    gender_id = alchemy.Column(alchemy.Integer, alchemy.ForeignKey(Gender.id), nullable=False)
    firstnames = alchemy.Column(alchemy.String, nullable=False)
    lastnames = alchemy.Column(alchemy.String, nullable=False)
    birthday = alchemy.Column(alchemy.String)
    active = alchemy.Column(alchemy.Boolean, default=True)

    #gender = alchemy.relationship("Gender", backref=alchemy.backref("personal", lazy="dynamic"))
    gender = alchemy.relationship(Gender, lazy='select')
    serialize_rules = ()

    def __init__(self, firstname, lastname, birthday, gender_id, type_id):
        self.firstnames = firstname
        self.lastnames = lastname
        self.birthday = birthday
        self.gender_id = gender_id
        self.type_id = type_id
        self.active = True
