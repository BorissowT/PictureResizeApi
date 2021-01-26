from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow.validate import Range


from db.database import Response
from service_functions import hash_id


class ResponseSchema(SQLAlchemySchema):
    identifier = fields.String(attribute="Identifier", required=True)
    image = fields.String(attribute="BaseCode", required=True)
    width = fields.Integer(attribute="Width", required=True)
    height = fields.Integer(attribute="Height", required=True)

    class Meta:
        model = Response


class RequestSchema(Schema):
    identifier = fields.Function(lambda obj: hash_id(obj["identifier"]))
    image = fields.String(required=True)
    width = fields.Integer(required=True, validate=Range(min=1,
                                                         min_inclusive=False,
                                                         max=2000,
                                                         max_inclusive=False))
    height = fields.Integer(required=True, validate=Range(min=1,
                                                          min_inclusive=False,
                                                          max=2000,
                                                          max_inclusive=False))



response_schema = ResponseSchema()
request_schema = RequestSchema()