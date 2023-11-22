from app.exception import UserMessageException
from flask import jsonify

def register_error_handler(app):
    @app.errorhandler(UserMessageException)
    def handle_error(error):
        response = {
            "message": error.message,
            "status": False
        }
        return jsonify(response), error.code