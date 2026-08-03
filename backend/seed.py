from app import app
from config import db
from models import User, Note

with app.app_context():
    print("Deleting existing data...")

    Note.query.delete()
    User.query.delete()

    print("Creating users...")

    brian = User(username="brian")
    brian.password_hash = "1234"

    alice = User(username="alice")
    alice.password_hash = "password"

    db.session.add_all([brian, alice])
    db.session.commit()

    print("Creating notes...")

    notes = [
        Note(
            title="Shopping",
            content="Buy milk and bread",
            user_id=brian.id
        ),
        Note(
            title="Homework",
            content="Finish Flask lab",
            user_id=brian.id
        ),
        Note(
            title="Workout",
            content="Gym at 6 PM",
            user_id=alice.id
        ),
    ]

    db.session.add_all(notes)
    db.session.commit()

    print("Database seeded successfully!")