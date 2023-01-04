from sys import path as sysPath
import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep
from datetime import datetime
import random

filepath = osPath.dirname(osPath.realpath(__file__))

connector = rti.Connector("MyParticipantLibrary::camera", filepath + "/DDS.xml")
outputDDS = connector.getOutput("cameraWriter::cameraTime")

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    outputDDS.instance.setString("cameraTime", current_time)
    outputDDS.write()
    print(f'The time is :  {current_time}')
    sleep(0.1)