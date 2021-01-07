# PictureResizeApi

create an API for the picture resizing. The service has to be an asynchronous.
That's mean all the requests has its own id number. User can get status of the operation by sending request to the address/api/{id}.
The API (address/api) requires a post request with text json in body as follows {"image":{base64 encoded picture},"width":{w}, "height":{h}}. Every part of application schould be containerized. 

Technologies:\
ajax for encoding picture.\
flask for handling requests.\
kafka confluence docker container for saving requests.\
mysql for saving results.\
docker container for service.\
marshmallow - to serialize data (is for hiding real db-column's names from clients)\
web server - werkzeug

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
1.create .env file in "PictureResizeApi/kafka_client/consumer_container/" as following:DB_MYSQL_REMOTE_USER=root\
DB_MYSQL_PASS=<pass>\
DB_MYSQL_ADD=192.168.1.103:3307\
KAFKA_TOPIC_NAME=<topic_name>\
KAFKA_GROUP_NAME=<group_id>\
2.run "docker-compose up" from "PictureResizeApi/kafka_client/consumer_container/".
  
Then you can send requests from localhost:5000 and check results at localhost:5000/api/
