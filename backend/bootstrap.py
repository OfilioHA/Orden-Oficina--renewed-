from flask import Flask
from app.Controllers import register_bps
from extensions.alchemy import register_db
from extensions.cors import register_cors
from extensions.guard import register_guard
from extensions.migrate import register_migrate
from extensions.errors import register_error_handler
import dotenv
dotenv.load_dotenv()

app = Flask(__name__)

register_bps(app)
register_db(app)
register_cors(app)
register_guard(app)
register_migrate(app)
register_error_handler(app)