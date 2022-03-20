import serial
from time import sleep

def get_dht22_data(request):
    # Connect to arduino
    arduino = serial.Serial('/dev/ttyUSB0', 9600)
    arduino.flush()
    data_sent = request.encode('utf-8')
    arduino.write(data_sent)
    sleep(0.60)
    temp = float(arduino.readline().decode('utf-8').split("\r")[0])
    # Close the serial connection
    # arduino.close()
    return temp
    
