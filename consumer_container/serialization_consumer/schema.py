from marshmallow import fields
from marshmallow.validate import Range
from marshmallow_sqlalchemy import SQLAlchemySchema
from db_consumer.database import Response


class ResponseSchema(SQLAlchemySchema):
    identifier = fields.String(attribute="Identifier", required=True)
    image = fields.String(attribute="BaseCode", required=True)
    width = fields.Integer(attribute="Width", required=True,
                           validate=Range(min=1,
                                          min_inclusive=False,
                                          max=2000,
                                          max_inclusive=False)
                           )
    height = fields.Integer(attribute="Height", required=True,
                            validate=Range(min=1,
                                           min_inclusive=False,
                                           max=2000,
                                           max_inclusive=False)
                            )

    class Meta:
        model = Response
        load_instance = True


response_schema = ResponseSchema()
