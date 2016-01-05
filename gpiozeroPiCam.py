from gpiozero import Button
from picamera import PiCamera
from signal import pause
import time

def capture():

    with PiCamera() as camera:

        time.sleep(2)

        camera.capture('/home/pi/Desktop/testing.jpg')



btn=Button(17)

btn.when_pressed = capture()

#pause()
