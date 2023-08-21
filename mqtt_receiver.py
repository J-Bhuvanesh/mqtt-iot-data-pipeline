import paho.mqtt.client as mqtt
import json
import pymongo


mongo_client = pymongo.MongoClient("mongodb://mqtt:mqtt@127.0.0.1:27017/iot")
print(mongo_client)
db = mongo_client["iot"]
print(db)
temperature_collection = db["sensors_temperature"]
humidity_collection = db["sensors_humidity"]

print(temperature_collection)
print(humidity_collection)



def on_message(client, userdata, message):
    payload = message.payload.decode('utf-8')
    topic = message.topic

    data = json.loads(payload)[0]
    print(f"Received message: {payload} on topic {topic}")

    # Store data in MongoDB
    if topic == topic_sensors_temperature:
        temperature_collection.insert_one(data)
    elif topic == topic_sensors_humidity:
        humidity_collection.insert_one(data)

# Define the MQTT broker settings
broker_address = "localhost"
port = 1883

topic_sensors_temperature = "sensors_temperature"
topic_sensors_humidity = "sensors_humidity"

# Create an MQTT client
client = mqtt.Client()
print("MQTT Client created : ", client)
print("MQTT Client type : ", type(client))

# Set the on_message callback function
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, port)

client.subscribe(topic_sensors_temperature)
client.subscribe(topic_sensors_humidity)

client.loop_forever()