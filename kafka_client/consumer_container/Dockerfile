FROM python:3.8
ARG topic_name
WORKDIR /app

ENV KAFKA_BROKER=broker:29092
ENV KAFKA_TOPIC_NAME=topic_test
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["kafka_consumer.py", "-container"]