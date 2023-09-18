import json
import time
import traceback

import paho.mqtt.client as mqtt

from common import get_sensor_data, mqtt_broker_address


def publish_mqtt_message():
    try:
        # MQTT broker configuration
        port = 1883
        topic_sensors_temperature = "sensors_temperature"
        topic_sensors_humidity = "sensors_humidity"

        # Retrieve sensor data
        sensors_humidity_list, sensor_temperature_list = get_sensor_data()
        print("Sensor data retrieved successfully")
        # sensor_temperature_list = [{"sensor_id": "1", "value": "90", "timestamp": "2023-08-20 20:00:00.000"}]

        # Prepare sensor data as JSON messages
        message_of_sensor_temperature = json.dumps(sensor_temperature_list)

        # sensors_humidity_list = [{"sensor_id": "1", "value": "25", "timestamp": "2023{"sensor_id": "1", "value": "90", "timestamp": "2023-08-20 20:00:00.000"}-08-20 20:00:00.000"}]

        # Prepare sensor data as JSON messages
        message_of_sensor_humidity = json.dumps(sensors_humidity_list)


        # Connect to the MQTT broker
        client = mqtt.Client()
        client.connect(mqtt_broker_address, port)


        # Publish sensor data to MQTT topics
        client.publish(topic_sensors_humidity, message_of_sensor_humidity)
        client.publish(topic_sensors_temperature, message_of_sensor_temperature)
        print("Stored the sensor data successfully")
        # Disconnect from the MQTT broker
        client.disconnect()
        print("Connection closed")
    except Exception as e:
        print("Error with MQTT publisher. Please check the below error traceback.")
        print(f"Host : {mqtt_broker_address}")
        print({"Error": str(e), "Error Traceback": traceback.format_exc()})

# Periodically publish sensor data
while True:
    publish_mqtt_message()
    time.sleep(10)
