from marshmallow import Schema, fields


class RequestSchema(Schema):
    Identifier = fields.String(required=True)
    BaseCode = fields.String(required=True)
    Width = fields.Integer(required=True)
    Height = fields.Integer(required=True)


request_schema = RequestSchema()
