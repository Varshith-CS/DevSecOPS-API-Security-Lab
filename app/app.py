from werkzeug.security import generate_password_hash, check_password_hash

import os
from dotenv import load_dotenv

from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

load_dotenv()

app = Flask(__name__)

JWT_SECRET = os.getenv("JWT_SECRET")
API_KEY = os.getenv("API_KEY")

users = {
    1: {"id": 1, "username": "jay", "password": generate_password_hash("password123"), "role": "user", "email": "jay@example.com"},
    2: {"id": 2, "username": "admin", "password": generate_password_hash( "admin123"), "role": "admin", "email": "admin@example.com"},
    3: {"id": 3, "username": "analyst", "password": generate_password_hash("analyst123"), "role": "user", "email": "analyst@example.com"}
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Authorization token is missing"}), 401

        token = auth_header.split(" ")[1]

        try:
            decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            request.current_user = decoded
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)
    return decorated

def sanitize_user(user):
    return {
        "id": user["id"],
        "username": user["username"],
        "role": user["role"],
        "email": user["email"]
    }

@app.route("/")
def home():
    return jsonify({
        "message": "DevSecOps API Security Lab",
        "status": "running"
    })

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    for user in users.values():

        if user["username"] == username and check_password_hash(
            user["password"],
            password
        ):

            token = jwt.encode({
                "user_id": user["id"],
                "role": user["role"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, JWT_SECRET, algorithm="HS256")

            return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/users/<int:user_id>", methods=["GET"])
@token_required
def get_user(user_id):
    current_user_id = request.current_user["user_id"]
    current_user_role = request.current_user["role"]

    if current_user_id != user_id and current_user_role != "admin":
        return jsonify({"error": "Access denied"}), 403

    user = users.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(sanitize_user(user))

@app.route("/admin", methods=["GET"])
@token_required
def admin_panel():
    if request.current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify({
        "message": "Welcome to the admin panel",
        "status": "authorized"
    })

@app.route("/transfer", methods=["POST"])
@token_required
def transfer_money():
    data = request.get_json()

    return jsonify({
        "message": "Transfer processed",
        "from_account": data.get("from_account"),
        "to_account": data.get("to_account"),
        "amount": data.get("amount")
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
