from flask_praetorian import Praetorian
import os

guard = Praetorian();

def register_guard(app):
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["JWT_ACCESS_LIFESPAN"] = {"hours": int(os.getenv("JWT_ACC_LFSPN"))}
    app.config["JWT_REFRESH_LIFESPAN"] = {"days": int(os.getenv("JWT_REF_LFSPN"))}
    #guard.init_app(app, User);