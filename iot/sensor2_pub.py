from sys import path as sysPath
import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep
import random
from datetime import datetime

filepath = osPath.dirname(osPath.realpath(__file__))

connector = rti.Connector("MyParticipantLibrary::sensor2", filepath + "/DDS.xml")
temperature_DDS = connector.getOutput("sensor2Writer::sensor2Actuator2")


while True:
    temperature_rand = round(random.uniform(0, 50), 1)

    temperature_DDS.instance.setNumber("temperature", temperature_rand)
    temperature_DDS.write()


    print(f'The temperature from sensor 2 is :  {temperature_rand}')
    sleep(0.1)
