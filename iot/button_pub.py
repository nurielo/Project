from sys import path as sysPath
import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep
import random
from datetime import datetime

filepath = osPath.dirname(osPath.realpath(__file__))

connector = rti.Connector("MyParticipantLibrary::button", filepath + "/DDS.xml")
outputDDS = connector.getOutput("buttonWriter::buttonStatus")

while True:
    status = "start"
    outputDDS.instance.setString("start", status)
    outputDDS.write()
    print(f'The status is start')
    print (datetime.now())
    sleep(20)
    status = "stop"
    outputDDS.instance.setString("start", status)
    outputDDS.write()
    print(f'The status is stop')
    print (datetime.now())
    sleep(5)

