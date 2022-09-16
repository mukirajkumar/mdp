# ===============================================================
# Script to manage communication with STM32F Board 
# ===============================================================

import serial
import time

class STM(object):

    # Initialise the connection with STM32F Board
    # Check the connection port again, baud rate = 115200
    def __init__(self, port='/dev/ttyUSB0'):
        self.port = port
        self.baudrate = 115200
        self.isConnected = False

    def connect(self):
        while not self.isConnected:
            try:
                print("Establishing connection with STM Board ...")

                # Create a Serial instance named 'ser'
                self.ser = serial.Serial(self.port, self.baudrate, timeout = 120)
                # Check if the serial instance is open
                if (self.ser.is_open):
                    print("[SUCCESSFUL CONNECTION]: Successfully established connection with STM Board.")
                    self.isConnected = True

            except Exception as e:
                print(f"[ERROR] Unable to establish connection with STM32 Board: {str(e)}")
                # Retry to connect
                print("Retrying to connect with STM Board ...")
                time.sleep(1)

    def disconnect(self):
        try:
            if (self.ser): #Check there is a serial instance created
                print("STM: Disconnecting from STM Board ...")
                self.ser.close()
                self.isConnected = False
        except Exception as e:
            print(f"[ERROR]: Unable to disconnect from STM Board: {str(e)}") 


    # Getter method - to check if connection with STM32F board is established
    def getisConnected(self):
        return self.isConnected
    
    #def callForStatus(self):
        
    # Read and process message
    def read(self):
        #print("STM READ")
        try:
            #print("In read STM")
            #data = ""
            #while data
         #   print("0.1 sleep")
          #  time.sleep(0.1)
            data = self.ser.read(1).decode("UTF-8")
           # print("Raw Data: ", data)
            if data == '' or data is None: # No data read
                return "No reply"
            print(f"[FROM STM] {data}")
            return data
            
        except Exception as e:
            print(f"[ERROR] STM Board read error: {str(e)}")


    # Write message
    def write(self, message):
        try:
            # Ensure connection is established before sending a message
            if self.isConnected:
                for char in message:
                    self.ser.write(char.encode('UTF-8'))
                    print(f"[SENT TO STM]: {char}")
                    time.sleep(0.1)
                    
                print("Before stm read:")
                #return self.read()
                
            else:
                print("[Error]  Connection with STM board is not established")
        except Exception as e:
            print("[Error] Unable to send message from STM: %s" % str(e))






