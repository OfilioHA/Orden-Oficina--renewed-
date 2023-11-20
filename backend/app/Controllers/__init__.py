from .person import person_bp
from .task import task_bp


def register_bps(app):
    app.register_blueprint(person_bp)
    app.register_blueprint(task_bp)
