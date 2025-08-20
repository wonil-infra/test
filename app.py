from flask import Flask, jsonify

APP_VERSION = "1.0.0"

def msg():
    return "Hello Jenkins via Docker!"

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(message=msg(), version=APP_VERSION)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

