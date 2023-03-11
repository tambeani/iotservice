# iotservice

This project focuses on ingesting raw IoT sensor data through an ETL pipeline into S3 buckets.

Block Diagram:<br/>
![alt text](https://github.com/tambeani/iotservice/blob/main/Block%20Diagram.png?raw=true)

### Data Flow:

1. Publishing sensor data on AWS IoT core using MQTT protocol
2. Funnel data from IoT core into AWS Kinesis Firehose
3. Executing ETL scripts on AWS Kinesis
4. Push refined raw data into S3 bucket

### Generator script:

Utilized a python-based script for dumping dummy IoT sensor data on AWS IoT core.

>Note: Before running the generator script follow below steps,

1. Register an IoT thing in AWS 
2. Add a certificate for registered thing 
3. Download the CA,private & certificate file
4. Place downloaded files in /generator directory

Another update we need to do, is to attach the correct policy to the AWS IoT Thing. For the initial phase we have a FullAccess policy, which can be fine-tuned in the future.

Policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iot:*",
      "Resource": "*"
    }
  ]
}
```

Run below code:<br/>
```
cd generator
python basicPubSub.py -e <Your AWS IoT custom endpoint> -r <Root CA file> -c <Certificate file> -k <Private key file>
```
> Note: Use below command to get your AWS IoT custom endpoint <br/> aws iot describe-endpoint --endpoint-type iot:Data-ATS --profile demo

**Published data:**
```
    [
      {
        "timestamp": "2022-03-15T14:25:00Z",
        "building": "Snell Library",
        "floor": "3",
        "room": "357",
        "temperature_sensorID": "temp_snell_357_001",
        "temperature_value": 23.5,
        "temperature_unit": "C"
      }
    ]
```







