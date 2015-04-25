__author__ = 'mna'

import RPi.GPIO as GPIO
import time


print(GPIO.RPI_INFO)
print("mode is " + str(GPIO.getmode()))

led_pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

p = GPIO.PWM(led_pin, 0.5)
p.start(1)
input('Press return to stop:')
p.stop()
#GPIO.cleanup()


p = GPIO.PWM(led_pin, 50)  # channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
#GPIO.cleanup()

input('Press return to stop:')

while True:
    GPIO.output(led_pin, True)
    time.sleep(0.1)
    GPIO.output(led_pin, False)
    time.sleep(0.1)

GPIO.cleanup()