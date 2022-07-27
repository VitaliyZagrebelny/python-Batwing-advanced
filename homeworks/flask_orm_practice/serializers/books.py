from marshmallow import Schema, fields
from marshmallow.validate import Length


class BookSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    title = fields.String(required=True, validate=Length(max=255))