from fastapi import FastAPI, Query, Path

from common import _get_redis_conn

import json

app = FastAPI()


@app.get("/sensor-readings")
async def get_sensor_readings(
        start_date: str = Query(..., description="Start date"),
        end_date: str = Query(..., description="End date"),
):
    projection = {"_id": False, "sensor_id": True, "value": True, "timestamp": True}
    from common import _get_mongo_connection
    client, db = _get_mongo_connection()

    temperature_collection = db['sensors_temperature']
    humidity_collection = db['sensors_humidity']
    temperature_readings = list(
        temperature_collection.find(
            {"timestamp": {"$gte": start_date, "$lte": end_date}},
            projection=projection
        )
    )
    humidity_readings = list(
        humidity_collection.find(
            {"timestamp": {"$gte": start_date, "$lte": end_date}},
            projection=projection
        )
    )
    return {
        "temperature_readings": temperature_readings,
        "humidity_readings": humidity_readings,
    }


@app.get("/last-ten-sensor-readings/{sensor_id}")
async def get_last_ten_sensor_readings(sensor_id: str = Path(..., description="Sensor ID")):
    try:
        sensors_temperature_redis_key = f"sensors_temperature_{sensor_id}"
        sensors_humidity_redis_key = f"sensors_humidity_{sensor_id}"

        redis_client = _get_redis_conn()

        raw_readings_of_sensors_temperature = redis_client.lrange(sensors_temperature_redis_key, 0, 9)
        raw_readings_of_sensors_humidity = redis_client.lrange(sensors_humidity_redis_key, 0, 9)

        humidity_readings = [json.loads(raw_reading) for raw_reading in raw_readings_of_sensors_humidity]
        temperature_readings = [json.loads(raw_reading) for raw_reading in raw_readings_of_sensors_temperature]

        return {
            "temperature_readings": temperature_readings,
            "humidity_readings": humidity_readings,
        }
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
