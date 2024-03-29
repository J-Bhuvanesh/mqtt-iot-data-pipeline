import json
import traceback

import paho.mqtt.client as mqtt

from common import _get_mongo_connection, store_latest_readings_for_a_sensor, mqtt_broker_address


# Define functions to insert data into MongoDB collections
def _insert_to_sensors_temperature(sensors_temperature_li):
    try:
        client, db = _get_mongo_connection()
        db["sensors_temperature"].insert_many(sensors_temperature_li)
        print("Data inserted to sensors_temperature topic")
        client.close()
        return {"status": True}
    except Exception as e:
        print("Error occurred at the time of '_get_mongo_connection'")
        print({"Error": str(e), "Error Traceback": traceback.format_exc()})
        return {"status": False}


def _insert_to_sensors_humidity(sensors_humidity_li):
    try:
        client, db = _get_mongo_connection()
        db["sensors_humidity"].insert_many(sensors_humidity_li)
        print("Data inserted to sensors_humidity topic")
        client.close()
        return {"status": True}
    except Exception as e:
        print("Error occurred at the time of '_get_mongo_connection'")
        print({"Error": str(e), "Error Traceback": traceback.format_exc()})
        return {"status": False}


# Define the function to receive MQTT messages

def receive_mqtt_message():
    try:
        # Callback function for handling MQTT messages
        def on_message(client, userdata, message):

            payload = message.payload.decode('utf-8')
            topic = message.topic

            data_list = json.loads(payload)
            print(f"Received message: {payload} on topic {topic}")
            # Insert data into MongoDB collections and update Redis
            if topic == topic_sensors_temperature:
                _insert_to_sensors_temperature(data_list)
                for payload in data_list:
                    redis_key = f"{topic}_{payload['sensor_id']}"
                    store_latest_readings_for_a_sensor(redis_key, {"sensor_id": payload['sensor_id'],
                                                                   "value": payload['sensor_id'],
                                                                   "timestamp": payload['timestamp']})
            elif topic == topic_sensors_humidity:
                _insert_to_sensors_humidity(data_list)
                for payload in data_list:
                    redis_key = f"{topic}_{payload['sensor_id']}"
                    store_latest_readings_for_a_sensor(redis_key, {"sensor_id": payload['sensor_id'],
                                                                   "value": payload['sensor_id'],
                                                                   "timestamp": payload['timestamp']})

        # MQTT broker configuration
        port = 1883
        topic_sensors_temperature = "sensors_temperature"
        topic_sensors_humidity = "sensors_humidity"
        # Create an MQTT client and set the message callback
        client = mqtt.Client()
        print("MQTT Client created : ", client)
        print("MQTT Client type : ", type(client))
        client.on_message = on_message
        # Connect to the MQTT broker and subscribe to topics
        client.connect(mqtt_broker_address, port)
        client.subscribe(topic_sensors_temperature)
        client.subscribe(topic_sensors_humidity)
        # Start the MQTT loop to listen for messages
        client.loop_forever()
    except Exception as e:


        print("Error with MQTT receiver. Please check the below error traceback.")
        print(f"Host : {mqtt_broker_address}")
        print({"Error": str(e), "Error Traceback": traceback.format_exc()})


receive_mqtt_message()
