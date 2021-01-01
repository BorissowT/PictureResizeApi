FROM python:3.8

WORKDIR /app

ENV KAFKA_BROKER=broker:29092
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["kafka_consumer.py"]