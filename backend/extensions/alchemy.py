from flask_sqlalchemy import SQLAlchemy
from libs.utils import get_root_folder
import os

alchemy = SQLAlchemy()

def register_db(app):
    basedir = get_root_folder()
    database = os.path.join(basedir, os.getenv("DB_ADDR"))
    database = os.path.abspath(database)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config['SQLALCHEMY_ECHO'] = True
    app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    alchemy.init_app(app)

    with app.app_context():
        alchemy.create_all()