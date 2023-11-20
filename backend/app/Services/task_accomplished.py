from extensions.alchemy import alchemy as db
from app.Entities import TaskAccomplished


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
    def from_person_dicts(personal, active_round):

        personal_list = []

        for entry in personal:

            tasklist = __class__.from_person(entry, active_round).all()

            entry = entry.to_dict(
                only=('id', 'firstnames', 'lastnames',),
            )

            entry['taskaccomplished'] = [
                task.to_dict(rules=('-personal',))
                for task in tasklist
            ]

            personal_list.append(entry)

        return personal_list
