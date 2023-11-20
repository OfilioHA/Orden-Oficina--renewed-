from extensions import alchemy as db
from app.Entities import Personal


class PersonalService():

    @staticmethod
    def create(firstname, lastname, birthday, gender_id, type_id):
        new_person = Personal(
            firstname,
            lastname,
            birthday,
            gender_id,
            type_id
        )
        db.session.add(new_person)
        db.session.commit()
        return new_person
