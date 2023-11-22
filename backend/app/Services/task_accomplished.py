from extensions.alchemy import alchemy as db
from app.Entities import TaskAccomplished
from app.Entities import TaskAccomplishedRepository


class TaskAccomplishedService():

    @staticmethod
    def create(task_id, actual_round_id, person_id, date, time):
        new_task = TaskAccomplished(
            task_id,
            actual_round_id,
            person_id,
            date,
            time
        )
        db.session.add(new_task)
        db.session.commit()
        return new_task

    @staticmethod
    def from_personal(personal, active_round):

        for index, person in enumerate(personal):
            task_list = TaskAccomplishedRepository.from_person(person, active_round).all()
            task_accomplished = [task.to_dict() for task in task_list]
            entry = person.to_dict(
                only=('id', 'firstnames', 'lastnames', 'gender_id'),
            )
            entry['task_accomplished'] = task_accomplished
            personal[index] = entry

        return personal
