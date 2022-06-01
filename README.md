# iotservice

Commands to setup the Mosquitto broker,publisher & subscriber(secure mode):

1. mosquitto -v -c broker.conf

- This command would start the broker

2. mosquitto_sub -t myTopic -u admin -P 12345678