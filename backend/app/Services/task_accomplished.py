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
    def from_person(personal, active_round):

        personal_list = []
        for entry in personal:
            task_list = TaskAccomplishedRepository.from_person(entry, active_round).all()
            task_accomplished =  [task.to_dict() for task in task_list]
            entry = entry.to_dict(
                only=('id', 'firstnames', 'lastnames', 'gender_id'),
            )
            entry['task_accomplished'] = task_accomplished
            personal_list.append(entry)

        return []
