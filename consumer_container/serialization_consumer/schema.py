from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema
from db_consumer.database import Response


class ResponseSchema(SQLAlchemySchema):
    identifier = fields.String(attribute="Identifier", required=True)
    image = fields.String(attribute="BaseCode", required=True)
    width = fields.Integer(attribute="Width", required=True)
    height = fields.Integer(attribute="Height", required=True)

    class Meta:
        model = Response
        load_instance = True


response_schema = ResponseSchema()
