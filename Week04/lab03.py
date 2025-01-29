# macOS python -m venv env && source env/bin/activate
# Windows python -m venv env && source env/Scripts/activate
#                                      env/Scripts/activate
# pip install flask
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def serve_files():
    return send_from_directory("templates", "index.html")

if __name__ == "__main__":
    port = 8002
    app.run(host="0.0.0.0", port=port)

