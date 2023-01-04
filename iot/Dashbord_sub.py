import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep


filepath = osPath.dirname(osPath.realpath(__file__))

connector = rti.Connector("MyParticipantLibrary::dashboard",  filepath + "/DDS.xml")
time_from_camera = connector.getInput("dashboardReader::timeCamera")
temperature_from_sensor1 = connector.getInput("dashboardReader::temperatureSensor1")
actuator1_status = connector.getInput("dashboardReader::actuatorStatus1")
temperature_from_sensor2 = connector.getInput("dashboardReader::temperatureSensor2")
actuator2_status = connector.getInput("dashboardReader::actuatorStatus2")

while True:
    time_from_camera.read()
    temperature_from_sensor1.read()
    actuator1_status.read()
    temperature_from_sensor2.read()
    actuator2_status.read()

    LengthOfTime = time_from_camera.samples.getLength()
    LengthOfStatus1 = actuator1_status.samples.getLength()
    LengthOftemp1 = temperature_from_sensor1.samples.getLength()
    LengthOfStatus2 = actuator2_status.samples.getLength()
    LengthOftemp2 = temperature_from_sensor2.samples.getLength()

    if LengthOfTime > 0 and LengthOfStatus1 > 0 and LengthOftemp1 > 0 and LengthOfStatus2 > 0 and LengthOftemp2 > 0:

    #Print camera
        current_time = time_from_camera.samples.getString(LengthOfTime-1, "cameraTime")
        print(f'Camera: < {current_time}  >')

    #Print actuator 1 status
        status1_list = list()
        for j in range(0, LengthOfStatus1,1):
            if actuator1_status.infos.isValid(j):
                status1_list.append(actuator1_status.samples.getString(j, "status"))
        print(f'Actuator 1:  {status1_list} ')
        status1_list.clear()

    # Print actuator 2 status
        status2_list = list()
        for j in range(0, LengthOfStatus2):
            if actuator2_status.infos.isValid(j):
                status2_list.append(actuator2_status.samples.getString(j, "status"))
        print(f'Actuator 2:  {status2_list} ')
        status2_list.clear()

    # Print sensor 1 temperature
        range_for_j = min(LengthOftemp1, 10)
        temp1_list = []
        for j in range(0, range_for_j - 1):
            if temperature_from_sensor1.infos.isValid(j):
                temp1_list.append(temperature_from_sensor1.samples.getNumber(LengthOftemp1-1, "temperature"))
                LengthOftemp1 = LengthOftemp1 - 1
        print(f'Extreme Temp. 1:  {temp1_list} ')

    # Print sensor 2 temperature
        range_for_k = min(LengthOftemp2, 10)
        temp2_list = []
        for k in range(0, range_for_k - 1):
            if temperature_from_sensor2.infos.isValid(k):
                temp2_list.append(temperature_from_sensor2.samples.getNumber(LengthOftemp2 - 1, "temperature"))
                LengthOftemp2 = LengthOftemp2 - 1
        print(f'Extreme Temp. 2:  {temp2_list} ')

    sleep(5)



