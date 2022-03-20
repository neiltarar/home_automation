import serial
import psycopg2
from time import sleep
from datetime import datetime

now = datetime.now()
today = datetime.today().strftime('%d-%m-%Y')


# def run_sql(sql, params):
#     # Connect to postgresql database
#     conn = psycopg2.connect("dbname= home_automation user=pi")
#     # Open a cursor to perform database operations
#     cur = conn.cursor()
#     # Execute a query
#     cur.execute(sql, params)
#     conn.commit()
#     cur.close()
#     conn.close()

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
arduino.flush()
data_sent = "read_temp".encode('utf-8')
print(data_sent)
# data_sent = "read_temp"
arduino.write(data_sent)
# sleep(0.60)
temp = arduino.readline()
print(temp)