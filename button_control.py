__author__ = 'mna'

import RPi.GPIO as GPIO
import subprocess
import time

print(GPIO.RPI_INFO)
print("mode is " + str(GPIO.getmode()))

next_button_pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(next_button_pin, GPIO.IN)
GPIO.setup(next_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Input state: " + str(GPIO.input(next_button_pin)))


def get_playlist_items():
    playlist_bytes, err = subprocess.Popen(["mpc", "playlist"], stdout=subprocess.PIPE).communicate()
    return playlist_bytes.decode().rstrip().split('\n')


def get_current_item_name():
    playlist_bytes, err = subprocess.Popen(["mpc", "current"], stdout=subprocess.PIPE).communicate()
    return playlist_bytes.decode().rstrip()


def my_callback(channel):
    playlist = get_playlist_items()
    current_item_name = get_current_item_name()
    if playlist.index(current_item_name) < len(playlist) - 1:
        subprocess.call(["mpc", "next"])
    else:
        subprocess.call(["mpc", "play", "1"])


GPIO.add_event_detect(next_button_pin, GPIO.RISING, callback=my_callback, bouncetime=300)

while True:
    time.sleep(60)

GPIO.cleanup()



