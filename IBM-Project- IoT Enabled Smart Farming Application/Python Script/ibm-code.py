#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
import requests
import json
myConfig = { 
    "identity": {
        "orgId": "drhkpn",
        "typeId": "Smart-Farmer",
        "deviceId":"9192"
    },
    "auth": {
        "token": "SO_kL5!_*299@q6i4r"
    }
}
def myCommandCallback(cmd):
  
  if(cmd.data['cm']=="flon"):
    print("-----Light 1 is ON-----")

  if(cmd.data['cm']=="floff"):
    print("-----Light 1 is OFF-----")

  if(cmd.data['cm']=="mton"):
    print("-----Motor is ON-----")

  if(cmd.data['cm']=="mtoff"):
    print("-----Motor is OFF-----")

  if(cmd.data['cm']=="slon"):
    print("-----Light 2 is ON-----")
   
  if(cmd.data['cm']=="sloff"):
    print("-----Light 2 is OFF-----")

  if(cmd.data['cm']=="fton"):
    print("-----Trap 1 is ON-----")

  if(cmd.data['cm']=="ftoff"):
    print("-----Trap 1 is OFF-----")

  if(cmd.data['cm']=="ston"):
    print("-----Trap 2 is ON-----")

  if(cmd.data['cm']=="stoff"):
    print("-----Trap 2 is OFF-----")

  if(cmd.data['cm']=="tton"):
    print("-----Trap 3 is ON-----")

  if(cmd.data['cm']=="ttoff"):
    print("-----Trap 3 is OFF-----")

  if(cmd.data['cm']=="futon"):
    print("-----Light 4 is ON-----")

  if(cmd.data['cm']=="futoff"):
    print("-----Trap 4 is OFF-----")

  if(cmd.data['cm']=="fvon"):
    print("-----Gate Valve 1 is ON-----")

  if(cmd.data['cm']=="fvoff"):
    print("-----Gate Valve 1 is OFF-----")

  if(cmd.data['cm']=="svon"):
    print("-----Gate Valve 2 is ON-----")

  if(cmd.data['cm']=="svoff"):
    print("-----Gate Valve 2 is OFF-----")

  if(cmd.data['cm']=="tvon"):
    print("-----Gate Valve 3 is ON-----")

  if(cmd.data['cm']=="tvoff"):
    print("-----Gate Valve 3 is OFF-----")

  if(cmd.data['cm']=="fuvon"):
    print("-----Gate Valve 4 is ON-----")

  if(cmd.data['cm']=="fuvoff"):
    print("-----Gate Valve 4 is OFF-----")

  if(cmd.data['cm']=="fivon"):
    print("-----Gate Valve 5 is ON-----")

  if(cmd.data['cm']=="fivoff"):
    print("-----Gate Valve 5 is OFF-----")
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
while(True):
  weatherdata = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Chennai&appid=3942dd61b26410206c466575e5addfbf')
  a=weatherdata.text
  b=json.loads(a)
  c=(b["main"]["temp"]-273.15)
  d=(b["main"]["humidity"])
  myData={'temp':c, 'humid':d}
  client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
  print("Published data Successfully: %s", myData)
  client.commandCallback = myCommandCallback
  time.sleep(2)
  print()
client.disconnect()

