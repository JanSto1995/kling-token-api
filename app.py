from flask import Flask, jsonify
import jwt
import time
import os

app = Flask(__name__)

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

@app.route("/kling-token", methods=["GET"])
def get_token():
    now = int(time.time())
    payload = {
        "iss": ACCESS_KEY,
        "iat": now,
        "exp": now + 1800
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jsonify({"token": token})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

