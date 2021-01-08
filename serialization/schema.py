from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema

from db.database import Response
from service_functions import hash_id


class ResponseSchema(SQLAlchemySchema):
    identifier = fields.String(attribute="Identifier", required=True)
    image = fields.String(attribute="BaseCode", required=True)
    width = fields.Integer(attribute="Width", required=True)
    height = fields.Integer(attribute="Height", required=True)

    class Meta:
        model = Response


def serialize_request(request):
    data_json = request.json
    hashed_id = hash_id(request.remote_addr)
    data_json["identifier"] = hashed_id
    return data_json

response_schema = ResponseSchema()

