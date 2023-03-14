import json
import random
import uuid
import time
from datetime import datetime

location="Northeastern University"
building={"Snell library": {"1":[101,110],"2":[201,210],"3":[301,310]} ,
          "Curry Center" : {"1":[121,129],"2":[210,231],"3":[323,345]} ,
          "Beharakis" :{"1":[113,123],"2":[205,210],"3":[312,318]}}

temprange=[5,50]
humidityrange=[10,90]
carbondioxiderange=[2,6]


def iotdatageneration():
    for buildkey,floor in building.items():
                for level,rooms in floor.items():
                    for currentroom in range (rooms[0],rooms[1]+1):
                            for currentParam in range(3):
                                    data=[]
                                    item={"id":str(uuid.uuid4().fields[-1])[:5]}
                                    item["timestamp"]=datetime.now().strftime("%H:%M:%S")
                                    item["location"]=location
                                    item["building"]=buildkey
                                    item["floor"]=level
                                    item["room"]=currentroom
                                    if(currentParam==0):
                                            item["temperature_sensorID"]="temp_"+buildkey+"_"+str(currentroom)
                                            item["temp_value :"]= str(random.randint(temprange[0], temprange[1]))
                                            item["temperature_unit"]="C"
                                    elif(currentParam==1):
                                            item["humidity_sensorID"]="humidity_"+buildkey+"_"+str(currentroom)
                                            item["humidity__value"]=str(random.randint(humidityrange[0], humidityrange[1]))
                                            item["humidity_unit"]="%"
                                    else:
                                            item["C02_sensorID"]="C02_"+buildkey+"_"+str(currentroom)
                                            item["C02_value"]=str(random.randint(carbondioxiderange[0], carbondioxiderange[1]))
                                            item["C02_unit"]="%"
                                    data.append(item)
                                    jsonData=json.dumps(data)
                                    print(jsonData)

                                                     
                        
starttime=time.time()
while True:
        iotdatageneration()
        time.sleep(60.0-((time.time()-starttime)%60.0))