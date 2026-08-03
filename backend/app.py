from flask import Flask
from flask_restful import Api

from config import Config, db, bcrypt, migrate, jwt
from models import User, Note
from resources.auth import Signup, Login, Me
from resources.notes import Notes, NoteByID

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

api = Api(app)

api.add_resource(Signup, "/signup")
api.add_resource(Login, "/login")
api.add_resource(Me, "/me")
api.add_resource(Notes, "/notes")
api.add_resource(NoteByID, "/notes/<int:id>")


@app.route("/")
def home():
    return {
        "message": "Productivity API is running!"
    }


if __name__ == "__main__":
    app.run(debug=True)