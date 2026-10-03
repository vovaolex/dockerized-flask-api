from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "service": "docker-project-1",
        "message": "Hello from Docker"
    }

@app.route("/health")
def health():
    return {
        "status": "ok"
    }

@app.route("/info")
def info():
    return {
        "environment": os.getenv("APP_ENV", "development"),
        "version": os.getenv("APP_VERSION", "1.0"),
        "hostname": socket.gethostname()
    }

@app.route("/write")
def write():
    with open("/data/message.txt", "w") as f:
        f.write("Hello from persistent storage")

    return {
        "status": "saved"
    }

@app.route("/read")
def read():
    try:
        with open("/data/message.txt", "r") as f:
            content = f.read()

        return {
            "message": content
        }
    except FileNotFoundError:
        return {
            "message": "No data found"
        }

app.run(host="0.0.0.0", port=5000)
