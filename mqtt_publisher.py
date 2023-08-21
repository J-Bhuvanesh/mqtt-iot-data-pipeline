
import paho.mqtt.client as mqtt
import json

broker_address = "localhost"
port = 1883
topic_sensors_temperature = "sensors_temperature"
topic_sensors_humidity = "sensors_humidity"

sensor_temperature_list=[{ "sensor_id": "1", "value": "90", "timestamp": "2023-08-20 20:00:00.000" }]
message_of_sensor_temperature = json.dumps(sensor_temperature_list)

sensors_humidity_list=[{ "sensor_id": "1", "value": "25", "timestamp": "2023-08-20 20:00:00.000" }]
message_of_sensor_humidity = json.dumps(sensors_humidity_list)

# Create a new MQTT client
client = mqtt.Client()

# Connect to the broker
client.connect(broker_address, port)

# Publish the message to the topic
client.publish(topic_sensors_humidity, message_of_sensor_humidity)
client.publish(topic_sensors_temperature, message_of_sensor_temperature)

# Disconnect from the broker
client.disconnect()