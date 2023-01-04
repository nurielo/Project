import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep
from datetime import datetime

filepath = osPath.dirname(osPath.realpath(__file__))

# Status input from button
connector = rti.Connector("MyParticipantLibrary::actuator2",  filepath + "/DDS.xml")
status_from_button = connector.getInput("actuator2Reader::buttonStatus")

# Temperature from sensor 1
# connector2 = rti.Connector("MyParticipantLibrary::actuator1", filepath + "/DDS.xml")
temp_from_sensor2 = connector.getInput("actuator2Reader::Sensor2Temperature")

# Writer to the Dashbord
# connector3 = rti.Connector("MyParticipantLibrary::actuator1", filepath + "/DDS.xml")
write_status_to_dash = connector.getOutput("actuator2Writer::actuator2Dashboard")

while True:
    status_from_button.read()
    temp_from_sensor2.take()

    numOfTemperatures = temp_from_sensor2.samples.getLength()
    numOfStatus = status_from_button.samples.getLength()

    ID_orin = '205768849'


    if numOfTemperatures > 0 and numOfStatus > 0 :
        for j in range(0, numOfTemperatures):
            #if status_from_button.infos.isValid(j):
                status_button = status_from_button.samples.getString(j , "start")
                temperature_sensor = temp_from_sensor2.samples.getNumber(j , "temperature")
                if status_button == 'stop':
                    # stop status
                    status_temp = 'Stopped'

                elif status_button == 'start':
                    if (temperature_sensor > 40) :
                    # status start
                        # extreme temperature and start
                        status_temp = 'Degraded'
                    else:
                        # good temperature and start
                        status_temp = 'Working'

                write_status_to_dash.instance.setString("ID", ID_orin)
                write_status_to_dash.instance.setString("status", status_temp)
                write_status_to_dash.write()
                print(f'The status of  actuator 2 is :  {status_temp}')
                print(f'The status of  button is :  {status_button}')
                print(f'The temperature is :  {temperature_sensor}')
                #print(datetime.now())










