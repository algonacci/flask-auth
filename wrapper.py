from flask import jsonify
from functools import wraps

admin = False


def admin_require(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if admin:
            return f(*args, **kwargs)
        else:
            return jsonify({
                "status": {
                    "code": 403,
                    "message": "Forbidden",
                },
                "data": None
            }), 403

    return decorated_function
