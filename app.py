from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from auth import auth
from wrapper import admin_require

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)


@app.errorhandler(429)
def too_many_requests(error):
    return jsonify({
        "status": {
            "code": 429,
            "message": "Too many requests"
        },
        "data": None,
    }), 429


@app.route("/")
@limiter.limit("5 per minute")
@auth.login_required
@admin_require
def index():
    return jsonify({
        "status": {
            "code": 200,
            "message": "Success fetching the API",
        },
        "data": None
    }), 200


if __name__ == "__main__":
    app.run()
