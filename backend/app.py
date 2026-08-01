from flask import Flask
from flask_restful import Api

from config import Config, db, bcrypt, migrate, jwt

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

api = Api(app)


@app.route("/")
def home():
    return {
        "message": "Productivity API is running!"
    }


if __name__ == "__main__":
    app.run(debug=True)