from extensions.alchemy import alchemy as db
from app.Entities import TaskRounds
from app.Entities import Task


class TaskRepository():

    @staticmethod
    def from_round(round_id):
        return Task.query\
            .join(TaskRounds)\
            .filter(
                TaskRounds.id == round_id
            )
