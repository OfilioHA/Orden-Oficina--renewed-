from .person import person_bp
from .task import task_bp
from .task_round import round_bp
from .auth import auth_bp

def register_bps(app):
    app.register_blueprint(auth_bp);
    app.register_blueprint(person_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(round_bp)