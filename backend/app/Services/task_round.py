from app.Entities import TaskRoundRepository
from app.Exceptions import TaskRoundFullTasks

MAX_AMOUNT = 3


class TaskRoundService():

    @staticmethod
    def last_round(id):
        return TaskRoundRepository.task_active_round(id)

    @staticmethod
    def validate_tasks_amount(actual_round, person):
        tasks_accomplished = TaskRoundRepository.person_tasks_active_round(
            actual_round,
            person
        )
        tasks_accomplished_amount = tasks_accomplished.count()
        if (tasks_accomplished_amount >= MAX_AMOUNT):
            raise TaskRoundFullTasks("Ronda cumplida")
