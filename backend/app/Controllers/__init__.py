from .person import person_bp

def register_bps(app):
    app.register_blueprint(person_bp);