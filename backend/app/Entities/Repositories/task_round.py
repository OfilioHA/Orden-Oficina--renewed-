from extensions import alchemy as db
from app.Entities import TaskAccomplished
from app.Entities import TaskRounds
from app.Entities import Task
from app.Entities import Personal


class TaskRoundRepository():

    @staticmethod
    def task_active_round(id):
        return TaskRounds.query\
            .join(Task)\
            .filter(Task.id == id)\
            .order_by(db.desc(TaskRounds.number))\
            .group_by(Task.id)\
            .first()

    @staticmethod
    def person_tasks_active_round(id, person):
        return TaskAccomplished.query\
            .join(TaskRounds, TaskAccomplished.task_round_id == TaskRounds.id)\
            .join(Personal, TaskAccomplished.personal_id == Personal.id)\
            .filter(
                TaskRounds.id == id,
                Personal.id == person,
            )
