import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
print('test line1')

arduino.flush()
print('test line2')

# data_sent = "read_temp".encode('utf-8')
print('test line3')
# arduino.write(data_sent)
# time.sleep(1)
# temp = arduino.readline().decode('utf-8').split("\r")[0]
# print(data_sent)
# arduino.close()


while True:
    arduino_message = arduino.readline().decode('utf-8')
    try:
        print('loop_test line')
        message = input("ask temp")
        cooked_message = arduino.write(message.encode('utf-8'))
        print(cooked_message)
        time.sleep(0.5)
        print(arduino_message.split("\r")[0])
        if(arduino_message.split("\r")[0])!= '':
            print(float(arduino_message.split("\r")[0]))
    except KeyboardInterrupt:
        arduino.close()
        break