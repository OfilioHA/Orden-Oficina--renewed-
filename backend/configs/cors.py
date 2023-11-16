from flask_cors import CORS

cors = CORS();

def register_cors(app):
    cors.init_app(app)