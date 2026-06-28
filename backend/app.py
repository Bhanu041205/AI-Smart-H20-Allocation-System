from flask import Flask
from flask_cors import CORS

from config import Config
from database import db

app = Flask(__name__)

app.config.from_object(Config)

from config import Config


db.init_app(app)

CORS(app)

@app.route("/")
def home():
    return {
        "message": "AI Smart H20 Allocation System Backend Running"
    }

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)