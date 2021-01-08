# PictureResizeApi

This is a distributed and horizontal scalable RESTFul API service.
Every part of this app could run on a separate server or in a cluster of servers.
The main goal of this project is to construct a sample of the Event Driven Architecture.

Technical Design Assignment:\
Create an API for picture-resizing operations one. The service has to be an asynchronous.
That's mean all the requests has its own id number. User can get status of the operation by sending request to the address/api/{id}.
The initial post request to "address/api" requires a json dictionary in body with following attributes: {"image":{base64 encoded picture},"width":{w}, "height":{h}}.
As soon, as the operation is done, the client can get the resized picture by sending a request to 
'/api/{id}', where "id" is status, received by initial post request.
Eventually, every part of the application should run in separate docker containers. 

Main elements:\

DB - is a simple pre-existing MySQL database with only one table and only one user.
You can configure the db with the adminer interface,
by running SQL queries directly in a browser. 

Kafka - is a cluster of zookeeper, kafka and additionally control-center to maintain in kafka topics, groups and so on.

API - is a simple flask app with two url for sending requests and getting result. 
All resize requests are pushed to the kafka-topic.
For the convenience this app has another url with a template for encoding a picture.

Kafka-consumer - is a service, which is listening to the kafka topic, resizes pictures and saves
to the DB-element.

DB\
1..create .env file in "/PictureResizeApi/db_container" as following: \
DB_MYSQL_PASS=<pass>\
2.run "docker-compose up -d" from "/PictureResizeApi/db_container" \
3.check if everything is working on localhost:8080 in adminer

Kafka\
1.run "docker-compose up -d" from "/PictureResizeApi/kafka_client" \
2.check if everything is working on localhost:9021 in control-center

Api\
1.create .env file in "/PictureResizeApi/" as following:\
DB_MYSQL_REMOTE_USER=root\
DB_MYSQL_PASS=<pass>\
DB_MYSQL_ADD=192.168.1.103:3307\
KAFKA_TOPIC_NAME=<topic name for producer>\
2.run "docker-compose up" from "/PictureResizeApi/". (if kafka and db are running and you've configured .env properly you should see Running on http://0.0.0.0:5000/)
  
Kafka_consumer\
1.create .env file in "PictureResizeApi/kafka_client/consumer_container/" as following:\
DB_MYSQL_REMOTE_USER=root\
DB_MYSQL_PASS=<pass>\
DB_MYSQL_ADD=192.168.1.103:3307\
KAFKA_TOPIC_NAME=<topic_name>\
KAFKA_GROUP_NAME=<group_id>\
2.run "docker-compose up" from "PictureResizeApi/kafka_client/consumer_container/".
  
Then you can send requests from localhost:5000 and check results at localhost:5000/api/
