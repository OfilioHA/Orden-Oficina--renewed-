from extensions.alchemy import alchemy;
from sqlalchemy_serializer import SerializerMixin;

class User(alchemy.Model, SerializerMixin):

    id = alchemy.Column(alchemy.Integer, primary_key=True)
    username = alchemy.Column(alchemy.String(18))
    password = alchemy.Column(alchemy.String(128))
    personal_id = alchemy.Column(alchemy.Integer, alchemy.ForeignKey('personal.id'), nullable=False, unique=True)
    is_active = alchemy.Column(alchemy.Boolean, default=True)
    roles = alchemy.Column(alchemy.String(50), default="user")
    
    serialize_rules = (
        '-password',
        '-personal_id',
    )

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        return self.is_active