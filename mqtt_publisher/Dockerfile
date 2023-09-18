

FROM python:3.9-slim

WORKDIR /app

COPY . .
RUN rm -rf venv
RUN python3 -m venv venv
RUN . venv/bin/activate

RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt



CMD ["python", "mqtt_publisher.py"]
