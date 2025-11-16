from flask import Blueprint, request, jsonify
from database.db import db
from database.models import Session
from datetime import datetime
from utils.jwt_helper import auth_required

session_bp = Blueprint("session", __name__)

@session_bp.route("/start", methods=["POST"])
@auth_required
def start_session(user):
    new_session = Session(user_id=user['id'])
    db.session.add(new_session)
    db.session.commit()

    return jsonify({
        "message": "Interview session started",
        "session_id": new_session.id,
        "status": new_session.status
    }), 201

@session_bp.route("/processing/<int:session_id>", methods=["POST"])
@auth_required
def processing_session(user, session_id):
    session = Session.query.get(session_id)

    if not session or session.user_id != user['id']:
        return jsonify({"error": "Invalid session"}), 404

    session.processing_time = datetime.utcnow()
    session.status = "processing"
    db.session.commit()

    return jsonify({"message": "Session is processing...", "session_id": session_id})

@session_bp.route("/complete/<int:session_id>", methods=["POST"])
@auth_required
def complete_session(user, session_id):
    session = Session.query.get(session_id)

    if not session or session.user_id != user['id']:
        return jsonify({"error": "Invalid session"}), 404

    session.completed_time = datetime.utcnow()
    session.status = "completed"
    db.session.commit()

    return jsonify({"message": "Session completed!", "session_id": session_id})

@session_bp.route("/<int:session_id>", methods=["GET"])
@auth_required
def get_session(user, session_id):
    session = Session.query.get(session_id)
    if not session or session.user_id != user['id']:
        return jsonify({"error": "Invalid session"}), 404
    return jsonify(session.to_dict())
