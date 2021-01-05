FROM python:3.8
ARG topic_name
WORKDIR /app

ENV KAFKA_BROKER=broker:29092
ENV KAFKA_TOPIC_NAME=topic_test
ENV KAFKA_GROUP_NAME=my-group-id
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["kafka_consumer.py", "-container"]