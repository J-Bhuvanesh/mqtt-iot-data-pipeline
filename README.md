# IoT Sensor Simulation Project

This project simulates the behavior of sensors, monitors their readings, and provides APIs to retrieve data based on specific criteria. It uses Docker Compose to integrate various services.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Building Custom Docker Images](#building-custom-docker-images)

## Prerequisites
Before you begin, ensure you have the following installed:
- Docker
- Docker Compose

## Getting Started

### Clone this repository:

To get started, clone the project repository and navigate to its directory:
```bash
git clone https://github.com/J-Bhuvanesh/mqtt-iot-data-pipeline.git
cd mqtt-iot-data-pipeline
```

## Usage:
    Start Docker compose:
        docker-compose up
    
    Stop Docker compose:
        docker-compose stop
        
    Steps to check the data:
    
    Use this below curl or api to check the data based on the certain time range:
        Api:
            http://localhost:8000/sensor-readings?start_date=2023-08-01T00:00:00&end_date=2023-09-31T23:59:59
        Curl:
            curl "http://localhost:8000/sensor-readings?start_date=2023-08-01T00:00:00&end_date=2023-09-31T23:59:59"
    
    Use this below curl or api to check the data based on sensor id:
        Api:
            http://localhost:8000/last-ten-sensor-readings/1
        Curl:
            curl http://localhost:8000/last-ten-sensor-readings/1
    
    
    
    Steps to build custom docker image:
        Steps tp bild mqtt-fast-api image:
            cd fast_api
            sudo docker build -t mqtt-fast-api .
        Steps tp bild mqtt-publisher image:
            cd mqtt_publisher
            sudo docker build -t mqtt-publisher .
        Steps tp bild mqtt-receiver image:
            cd mqtt_receiver
            sudo docker build -t mqtt-receiver .
        Once after building custom images please change in the docker compose file accordingly