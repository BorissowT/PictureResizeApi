# PictureResizeApi

create an API for picture resizing. The service has to be an asynchronous.
That's mean all of requests has its own id number. User can get status of the operation by sending request to the address/api/{id}.
The API (address/api) requires an post request with text json in body as follow {"image":{base64 encoded picture},"width":{w}, "height":{h}}.

Technologies:
ajax for encoding picture.
flask for handling requests.
kafka for saving requests.
mysql for saving results.
