# backend/app.py

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {
        "status": "running",
        "project": "AI Smart H20 Allocation System"
    }

if __name__ == "__main__":
    app.run(debug=True)