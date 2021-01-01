# PictureResizeApi

create an API for picture resizing. The service has to be an asynchronous.
That's mean all of requests has its own id number. User can get status of the operation by sending request to the address/api/{id}.
The API (address/api) requires an post request with text json in body as follow {"image":{base64 encoded picture},"width":{w}, "height":{h}}.

Technologies:\
ajax for encoding picture.\
flask for handling requests.\
kafka confluence docker container for saving requests.\
mysql for saving results.\
docker container for service.

to start the app you should:
1) install docker engine:
2) from workdir execute command: docker docker-compose up or docker-compose up -d 
3) sometimes broker starts too slow or doesn't start because of slow zookeeper. thence try to start broker container and then pictureapi_web_1 again
4) proceed to localhost:5000

to start a consumer:\
1)execute two commands in kafka_client/consumer_container directory in kafka_client_commands.txt
