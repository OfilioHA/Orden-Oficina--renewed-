from flask_praetorian import Praetorian
from app.Entities import User
from extensions.alchemy import alchemy as db
import os

guard = Praetorian()


def register_guard(app):
    with app.app_context():
        app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
        app.config["JWT_ACCESS_LIFESPAN"] = {"hours": int(os.getenv("JWT_ACC_LFSPN"))}
        app.config["JWT_REFRESH_LIFESPAN"] = {"days": int(os.getenv("JWT_REF_LFSPN"))}
        guard.init_app(app, User)
        create_user()

def create_user():
    username = "testing"
    password = "password"

    user = db.session.query(User).filter_by(username=username).first()

    if not user:
        new_user = User()
        new_user.username = username
        new_user.password = guard.hash_password(password)
        new_user.personal_id = 1
        db.session.add(new_user)
        db.session.commit()
