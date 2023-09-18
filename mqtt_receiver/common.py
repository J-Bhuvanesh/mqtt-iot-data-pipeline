import json
import random
import traceback
from datetime import datetime
import os
import pymongo
import redis
from dotenv import load_dotenv

load_dotenv()
redish_host = os.getenv("redish_host", "localhost")
mongo_host = os.getenv("mongo_host", "localhost")
mqtt_broker_address = os.getenv("mqtt_broker_address","localhost")


def generate_sensor_payload(sensor_id):
    humidity_value = round(random.uniform(20, 80), 2)
    temperature_value = round(random.uniform(70, 100), 2)

    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    humidity_payload = {
        "sensor_id": sensor_id,
        "value": str(humidity_value),
        "timestamp": current_timestamp
    }

    temperature_payload = {
        "sensor_id": sensor_id,
        "value": str(temperature_value),
        "timestamp": current_timestamp
    }

    return humidity_payload, temperature_payload


def get_sensor_data():
    humidity_payload_list = []
    temperature_payload_list = []
    for i in range(1, 21):
        humidity_payload, temperature_payload = generate_sensor_payload(i)
        humidity_payload_list.append(humidity_payload)
        temperature_payload_list.append(temperature_payload)
    return humidity_payload_list, temperature_payload_list


def _get_mongo_connection():
    mongodb_url = f"mongodb://{mongo_host}:27017"
    db_name = "iot"
    client = pymongo.MongoClient(mongodb_url)
    db = client[db_name]
    return client, db


def _get_redis_conn():
    redis_client = redis.StrictRedis(host=redish_host, port=6379, db=0)
    return redis_client


def store_latest_readings_for_a_sensor(redis_key, data_list):
    try:
        print(redis_key)
        print(data_list)
        json_data = json.dumps(data_list)
        redis_client = _get_redis_conn()
        redis_client.lpush(redis_key, json_data)
        redis_client.ltrim(redis_key, 0, 9)
        return {}
    except Exception as e:
        print("Error occurred while storing data in Redis")
        print({"Error": str(e), "Error Traceback": traceback.format_exc()})
        return {}
