from .flask import app
from app.Controllers import register_bps
from .alchemy import register_db
from .cors import register_cors
import dotenv
dotenv.load_dotenv()

register_bps(app)
register_db(app)
register_cors(app)