from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

# Intentionally hardcoded secret for DevSecOps scanning demo
JWT_SECRET = "super-secret-dev-key-123"
API_KEY = "sk_test_hardcoded_fake_key_12345"

users = {
    1: {"id": 1, "username": "jay", "password": "password123", "role": "user", "email": "jay@example.com"},
    2: {"id": 2, "username": "admin", "password": "admin123", "role": "admin", "email": "admin@example.com"},
    3: {"id": 3, "username": "analyst", "password": "analyst123", "role": "user", "email": "analyst@example.com"}
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
        if user["username"] == username and user["password"] == password:
            token = jwt.encode({
                "user_id": user["id"],
                "role": user["role"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, JWT_SECRET, algorithm="HS256")

            return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    # Vulnerable: Broken Object Level Authorization
    user = users.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)

@app.route("/admin", methods=["GET"])
def admin_panel():
    # Vulnerable: Missing role validation
    return jsonify({
        "message": "Welcome to the admin panel",
        "sensitive_config": {
            "api_key": API_KEY,
            "debug": True
        }
    })

@app.route("/transfer", methods=["POST"])
def transfer_money():
    # Vulnerable: no auth, no validation, no rate limiting
    data = request.get_json()

    return jsonify({
        "message": "Transfer processed",
        "from_account": data.get("from_account"),
        "to_account": data.get("to_account"),
        "amount": data.get("amount")
    })

@app.route("/debug", methods=["GET"])
def debug_info():
    # Vulnerable: sensitive internal data exposure
    return jsonify({
        "debug": True,
        "jwt_secret": JWT_SECRET,
        "api_key": API_KEY,
        "users": users
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
