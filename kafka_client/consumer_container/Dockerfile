FROM python:3.8
ARG topic_name
WORKDIR /kafka_client/consumer_container

ENV KAFKA_BROKER=broker:29092
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["kafka_consumer.py", "-container"]