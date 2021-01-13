# PictureResizeApi

This is a distributed and horizontal scalable RESTFul API service.
Every part of this app could run on a separate server or in a cluster of servers (alternatively
all elements could run on a single machine).
The main goal of this project is to construct a sample of the Event Driven Architecture.

Technical Design Assignment:\
Create an API for picture-resizing operations one. The service has to be an asynchronous.
That's mean all the requests has its own id number. User can get status of
the operation by id or the result of the operation.
The initial POST request to "address/api" requires a json dictionary in body with following attributes: {"image":{base64 encoded picture},"width":{w}, "height":{h}}.
As soon, as the operation is done, the client can get the resized picture by sending a GET request to the API
with id in the body. Eventually, every part of the application should run in separate docker containers. 

Main elements:\

DB - is a simple pre-existing MySQL database with only one table and only one user.
You can configure the db with the adminer interface,
by running MySQL scripts directly in a browser. 

Kafka - is a cluster of zookeeper, kafka and additionally control-center to maintain kafka's elements.

API - is a simple flask app with two url for sending requests and getting result. 
All resize requests are pushed to the kafka-topic.
For the convenience this app has another url with a template for making requests to API.

Kafka-consumer - is a service, which is listening to the kafka topic, resizes pictures and saves
in the DB-element.

