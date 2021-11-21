import RPi.GPIO as GPIO

import requests

import threading
import time

LOW = GPIO.LOW
HIGH = GPIO.HIGH

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(9, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(8, GPIO.IN)

# Currently, not used
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, LOW)

print('Ben says to \"log shit\"...\nFine')

def error_thread():
    for i in range(24):
        GPIO.output(14, (i + 1) % 2)
        time.sleep(0.2)


while True:
    if GPIO.input(9):
        try:
            print('Attempting rehearsal on...')
            r = requests.get('http://txlight.ystv.york.ac.uk/?rehearsal_on')
            if not r.status_code == 204:
                print('Rehearsal on fail!')
                error = threading.Thread(target=error_thread)
                error.start()
            else:
                print('Rehearsal on success!')
        except:
            error = threading.Thread(target=error_thread)
            error.start()
    if GPIO.input(25):
        try:
            print('Attempting transmission on...')
            r = requests.get('http://txlight.ystv.york.ac.uk/?transmission_on')
            if not r.status_code == 204:
                print('Transmission on fail!')
                error = threading.Thread(target=error_thread)
                error.start()
            else:
                print('Transmission on success!')
        except:
            error = threading.Thread(target=error_thread)
            error.start()
    if GPIO.input(11):
        try:
            print('Attempting rehearsal transmission on...')
            r = requests.get('http://txlight.ystv.york.ac.uk/?rehearsal_transmission_on')
            if not r.status_code == 204:
                print('Rehearsal transmission on fail!')
                error = threading.Thread(target=error_thread)
                error.start()
            else:
                print('Rehearsal transmission on success!')
        except:
            error = threading.Thread(target=error_thread)
            error.start()
    if GPIO.input(8):
        try:
            print('Attempting rehearsal transmission off...')
            r = requests.get('http://txlight.ystv.york.ac.uk/?rehearsal_transmission_off')
            if not r.status_code == 204:
                print('Rehearsal transmission off fail!')
                error = threading.Thread(target=error_thread)
                error.start()
            else:
                print('Rehearsal transmission off success!')
        except:
            error = threading.Thread(target=error_thread)
            error.start()
