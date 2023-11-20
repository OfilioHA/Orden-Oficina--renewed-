from extensions import alchemy as db
from app.Entities import Personal
from app.Entities import PersonalRepository


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

    @staticmethod
    def from_task(id):
        query = PersonalRepository.from_task(id)
        return query.all()
