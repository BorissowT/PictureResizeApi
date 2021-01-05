# PictureResizeApi

create an API for picture resizing. The service has to be an asynchronous.
That's mean all of requests has its own id number. User can get status of the operation by sending request to the address/api/{id}.
The API (address/api) requires an post request with text json in body as follow {"image":{base64 encoded picture},"width":{w}, "height":{h}}.

Technologies:\
ajax for encoding picture.\
flask for handling requests.\
kafka confluence docker container for saving requests.\
mysql for saving results.\
docker container for service.\
web server - werkzeug

to start the app you should:
1) install docker engine:
2) from workdir execute command: docker-compose up or docker-compose up -d (p.s. you can specify kafka topic for the producer on this step by modifying variable in .env file)
3) sometimes broker starts too slow or doesn't start because of slow zookeeper. thence try to start broker container and then pictureapi_web_1 again
4) proceed to localhost:5000 or execute "docker logs pictureapi_web_1" (you'll see: Running on http://0.0.0.0:5000/)

to start a consumer:\
1)execute first command from kafka_client_commands in consumer's directory
2)execute second command. Note, that you can to specify topic's name and group's name for the consumer on this step, by setting environment variables. By default it set to "topic_test" and "my-group-id", respectively.