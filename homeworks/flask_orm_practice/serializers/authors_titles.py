from marshmallow import Schema, fields


class AuthorsTitlesSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    author = fields.String(required=True)
    title = fields.String(required=True)
