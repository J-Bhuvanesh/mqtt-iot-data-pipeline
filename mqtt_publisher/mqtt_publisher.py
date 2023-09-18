import time

import paho.mqtt.client as mqtt
import json
from common import get_sensor_data
import traceback


def publish_mqtt_message():
    try:
        broker_address = "localhost"
        port = 1883
        topic_sensors_temperature = "sensors_temperature"
        topic_sensors_humidity = "sensors_humidity"
        sensors_humidity_list,sensor_temperature_list=get_sensor_data()
        print("Sensor data retrieved successfully")
        # sensor_temperature_list = [{"sensor_id": "1", "value": "90", "timestamp": "2023-08-20 20:00:00.000"}]
        message_of_sensor_temperature = json.dumps(sensor_temperature_list)

        # sensors_humidity_list = [{"sensor_id": "1", "value": "25", "timestamp": "2023{"sensor_id": "1", "value": "90", "timestamp": "2023-08-20 20:00:00.000"}-08-20 20:00:00.000"}]
        message_of_sensor_humidity = json.dumps(sensors_humidity_list)

        client = mqtt.Client()

        client.connect(broker_address, port)

        client.publish(topic_sensors_humidity, message_of_sensor_humidity)
        client.publish(topic_sensors_temperature, message_of_sensor_temperature)
        print("Stored the sensor data successfully")
        client.disconnect()
        print("Connection closed")
    except Exception as e:
        print("Error with MQTT publisher. Please check the below error traceback")
        print({"Error":str(e),"Error Traceback":traceback.format_exc()})



while True:
    publish_mqtt_message()
    time.sleep(10)