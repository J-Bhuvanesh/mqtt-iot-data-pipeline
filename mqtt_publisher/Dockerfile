
FROM python:3.9-slim

WORKDIR /app

RUN python3.9 -m pip install pip --upgrade
COPY . .

RUN pip install -r requirements.txt


CMD ["python", "mqtt_publisher.py"]
