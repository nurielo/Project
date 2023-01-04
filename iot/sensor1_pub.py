from sys import path as sysPath
import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep
import random
from datetime import datetime

filepath = osPath.dirname(osPath.realpath(__file__))

connector = rti.Connector("MyParticipantLibrary::sensor1", filepath + "/DDS.xml")
temperature_DDS= connector.getOutput("sensor1Writer::sensor1Actuator1")


while True:
    temperature_rand = round(random.uniform(10, 60), 1)

    temperature_DDS.instance.setNumber("temperature", temperature_rand)
    temperature_DDS.write()


    print(f'The temperature from sensor 1 is :  {temperature_rand}')
    sleep(1)
