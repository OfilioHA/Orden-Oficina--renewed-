import os
from flask_migrate import Migrate
from .alchemy import alchemy

migrate = False;

def register_migrate(app):
    migrate = Migrate(db=alchemy, directory=os.getenv('MG_ADDR'))
    migrate.init_app(app)