import http

import jwt
from flask import Blueprint, request, jsonify

from config import Config
from core.auth import token_required
from core.database import db
from core.models import Event, User, UserEvent
from event.serializer import EventSerializer, EventInvitationSerializer, RespondSerializer

from sqlalchemy import create_engine

event_router = Blueprint("event", __name__, url_prefix="/event")


@event_router.route("", methods=["GET"])
@token_required
def get(user):
    schema = EventSerializer(many=True)
    events = Event.query.filter(
        Event.users.any(
            User.id == user.id
        )
    )
    # db.session.query(Event).join(UserEvent).filter(UserEvent.user_id == user.id)
    # SELECT * FROM event JOIN user_event ON event.id = user_event.event_id WHERE user_event.user_id = 1
    events_json = schema.dump(events)
    return jsonify(events_json)


@event_router.route("/<int:event_id>", methods=["GET"])
@token_required
def retrieve(user, event_id):
    schema = EventSerializer()
    event = Event.query.filter(
        Event.users.any(
            User.id == user.id
        )
    ).filter(Event.id == event_id).first()
    # SELECT * FROM event
    # JOIN user_event ON event.id = user_event.event_id
    # WHERE user_event.user_id = 1 AND event.id = event_id

    events_json = schema.dump(event)
    return jsonify(events_json)


@event_router.route("", methods=["POST"])
@token_required
def create(user):
    data = request.get_json()
    schema = EventSerializer()
    event_data = schema.load(data)
    event_obj = Event(
        name=event_data["name"],
        description=event_data["description"],
        starts_at=event_data["starts_at"],
        ends_at=event_data["ends_at"]
    )
    event_obj.users.append(user)
    db.session.add(event_obj)
    db.session.commit()
    event_json = schema.dump(event_obj)
    return event_json


@event_router.route("/<int:event_id>/invite", methods=["POST"])
@token_required
def invite(user, event_id):
    data = request.get_json()
    event_schema = EventSerializer()
    invitation_schema = EventInvitationSerializer()
    invitation_data = invitation_schema.load(data)
    event = Event.query.filter(
        Event.users.any(
            User.id == user.id
        )
    ).filter(Event.id == event_id).first()
    if not event:
        return "No event found"

    for user_id in invitation_data["users_id"]:
        invited_user = User.query.get(user_id)
        if invited_user:
            event.users.append(invited_user)

    db.session.add(event)
    db.session.commit()
    event_json = event_schema.dump(event)
    return event_json


@event_router.route("/<int:event_id>/respond", methods=["POST"])
@token_required
def respond_to_invitation(user, event_id):
    STATUS = ['accepted, declined']
    data = request.get_json()
    respond_schema = RespondSerializer()
    respond_data = respond_schema.load(data)

    token = request.headers.get("Authorization")
    user_data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
    res_data = respond_data["event_respond"].lower()
    if res_data in STATUS:
        status = str("'" + res_data + "'")
        engine = create_engine(Config.SQLALCHEMY_DATABASE_URL, echo=False)
        current_status = engine.execute(f"SELECT invitation_status FROM user_event "
                                        f"WHERE (user_event.event_id = {event_id}"
                                        f"AND user_event.user_id = {user_data['user_id']})")
        res = current_status.fetchone()
        if res["invitation_status"] == "pending":
            engine.execute(f"UPDATE user_event SET invitation_status = {status} "
                           f"WHERE (user_event.event_id = {event_id} AND user_event.user_id = {user_data['user_id']})")
            return f"You {res_data} this event"
        else:
            return "You can't accept or decline this event", http.HTTPStatus.BAD_REQUEST
    else:
        return "Wrong answer", http.HTTPStatus.BAD_REQUEST


@event_router.route("/<int:event_id>/edit", methods=["POST"])
@token_required
def edit_event(user, event_id):
    data = request.get_json()
    schema = EventSerializer()
    event_data = schema.load(data)

    token = request.headers.get("Authorization")
    user_data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])

    event = Event.query.filter(Event.id == event_id).first()

    if not event:
        return "Not found", http.HTTPStatus.BAD_REQUEST

    if user_data['user_id'] == event.creator_id:
        event.name = event_data["name"]
        event.description = event_data["description"]
        event.starts_at = event_data["starts_at"]
        event.ends_at = event_data["ends_at"]

        db.session.commit()

        event_json = schema.dump(event)

        return event_json, http.HTTPStatus.CREATED

    else:
        return "You can't this edit event", http.HTTPStatus.FORBIDDEN


@event_router.route("/<int:event_id>/delete", methods=["POST"])
@token_required
def delete_event(user, event_id):
    token = request.headers.get("Authorization")
    user_data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])

    event = Event.query.filter(Event.id == event_id).first()

    if not event:
        return "No event found", http.HTTPStatus.BAD_REQUEST

    if user_data['user_id'] == event.creator_id:
        UserEvent.query.filter(UserEvent.event_id == event_id).delete()
        Event.query.filter(Event.id == event_id).delete()

        db.session.commit()
        return "Deleting completed"

    else:
        return "You can't delete this event", http.HTTPStatus.FORBIDDEN
