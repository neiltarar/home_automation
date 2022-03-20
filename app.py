from models.read_data import get_dht22_data
from flask import Flask, render_template
import os
from dotenv import load_dotenv
import requests
import serial
from time import sleep
load_dotenv()

#message = os.getenv("TEST")
#print(message)

app = Flask(__name__)

@app.route("/")
def home():
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    arduino.flush()
    temp = arduino.readline().decode('utf-8').split("\r")[0]
    print(temp)
    arduino.close()
    return render_template('index.html', temp = temp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8500")