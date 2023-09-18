

FROM ubuntu:latest
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN python3 -m pip install --upgrade pip
RUN rm -rf venv
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt


CMD ["python", "mqtt_publisher.py"]
