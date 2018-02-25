# interface will be serial
# Raspberry Pi serial is ???
# use pySerial?

import serial

class IndoorGPS:
    def __init__(self, port = '/dev/ttyUSB0'):
        self.comms = serial.Serial(port)
        #callback

    def serialCallback(self, data):
        processData(data)
        print("Serial -> " + data)

    def processData(self, data):
        #process serial data

        #raise event for complete message

    def msgCallbacl(self, cmd):



    def cleanup(self):
        self.comms.close()

    def sendCommand(self, cmd):

    def readCommand(self):

