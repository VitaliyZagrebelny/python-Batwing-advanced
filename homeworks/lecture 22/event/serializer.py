from marshmallow import Schema, fields

from user.serializer import UserSerializer


class EventSerializer(Schema):
    id = fields.Integer(required=True, dump_only=True)
    name = fields.String(required=True)
    description = fields.String()
    starts_at = fields.DateTime()
    ends_at = fields.DateTime()
    users = fields.List(fields.Nested(UserSerializer))
    creator_id = fields.Integer


class EventInvitationSerializer(Schema):
    users_id = fields.List(fields.Integer)


class RespondSerializer(Schema):
    event_res = fields.String
