from apscheduler.schedulers.blocking import BlockingScheduler
import serial

def read_dht22():
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    arduino.flush()
    temp = arduino.readline().decode('utf-8').split("\r")[0]
    print(temp)
    arduino.close()


scheduler = BlockingScheduler()
scheduler.add_job(read_dht22, 'interval', seconds=2)
scheduler.start()
