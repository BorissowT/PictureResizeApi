import base64
from io import BytesIO

from PIL import Image

from db_consumer.database import session
from serialization_consumer.schema import response_schema


def resize_picture(data_json):
    try:
        binary_image = base64.b64decode(data_json["image"])
        pil_image = Image.open(BytesIO(binary_image))
        resized_image = pil_image.resize((int(data_json["width"]), int(data_json["height"])))
        byte_stream = BytesIO()
        resized_image.save(byte_stream, format='PNG')
    except Exception as e:
        print(e)
    else:
        resized_img_str = base64.b64encode(byte_stream.getvalue())
        data_json["image"] = resized_img_str


def serialize_data(data_json):
    try:
        result = response_schema.load(data_json, session=session)
    except Exception as e:
        print(e)
    else:
        print("schema is loaded")
        return result


def add_to_db(result):
    try:
        session.add(result)
        session.commit()
    except Exception as e:
        print(e)
    else:
        print("successfully created")