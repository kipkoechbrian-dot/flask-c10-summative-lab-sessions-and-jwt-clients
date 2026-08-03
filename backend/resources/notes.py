from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from config import db
from models import Note
from schemas import note_schema, notes_schema


class Notes(Resource):

    @jwt_required()
    def get(self):
        current_user_id = int(get_jwt_identity())

        notes = Note.query.filter_by(user_id=current_user_id).all()

        return notes_schema.dump(notes), 200

    @jwt_required()
    def post(self):
        current_user_id = int(get_jwt_identity())

        data = request.get_json()

        title = data.get("title")
        content = data.get("content")

        if not title or not content:
            return {"error": "Title and content are required."}, 400

        note = Note(
            title=title,
            content=content,
            user_id=current_user_id
        )

        db.session.add(note)
        db.session.commit()

        return note_schema.dump(note), 201


class NoteByID(Resource):

    @jwt_required()
    def patch(self, id):

        current_user_id = int(get_jwt_identity())

        note = Note.query.filter_by(
            id=id,
            user_id=current_user_id
        ).first()

        if not note:
            return {"error": "Note not found."}, 404

        data = request.get_json()

        if "title" in data:
            note.title = data["title"]

        if "content" in data:
            note.content = data["content"]

        db.session.commit()

        return note_schema.dump(note), 200

    @jwt_required()
    def delete(self, id):

        current_user_id = int(get_jwt_identity())

        note = Note.query.filter_by(
            id=id,
            user_id=current_user_id
        ).first()

        if not note:
            return {"error": "Note not found."}, 404

        db.session.delete(note)
        db.session.commit()

        return {"message": "Note deleted successfully."}, 200