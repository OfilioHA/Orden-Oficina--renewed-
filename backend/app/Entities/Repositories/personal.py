from app.Entities import Personal
from app.Entities import Gender
from app.Entities import TaskCan
from app.Entities import Task


class PersonalRepository():

    @staticmethod
    def from_task(task_id, women=False):

        personal = Personal.query\
            .join(Gender)\
            .join(TaskCan)\
            .join(Task)\
            .filter(Task.id == task_id)

        if (not women):
            personal.filter(Gender.id != 2)

        return personal.all()
