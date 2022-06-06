# iotservice

This miniproject focusses on ingesting raw IoT sensor data through an ETL pipeline into S3 buckets.

Block Diagram:<br/>
![alt text](https://github.com/tambeani/iotservice/blob/main/Block%20Diagram.png?raw=true)

### Data Flow:

1. Publishing sensor data on AWS IoT core using MQTT protocol
2. Funnel data from IoT core into AWS Kinesis Firehose
3. Executing ETL scripts on AWS Kinesis
4. Push refined raw data into S3 bucket

### Generator script

Utilized a python-based script for dumping dummy IoT sensor data on AWS IoT core.

**Note:**  Before running the generator script follow below steps,
1. Register an IoT thing in AWS 
2. Add a certificate for registered thing 
3. Download the CA,private & certificate file
4. Place downloaded files in /generator

Run below code:<br/>
```
cd generator
python basicPubSub.py -e <Your AWS IoT custom endpoint> -r <Root CA file path> -c <Certificate file path> -k <Private key file path>
```
**Published data:**
```
{
    "description": "Assemlby Floor",
    "value": 30,
    "lat": 10,
    "lng": 90,
    "type": "temperature",
    "id": "Sensor 4",
    "unit": "C"
}
```







