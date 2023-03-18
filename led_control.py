import Jetson.GPIO as GPIO
import time

class LED_Controller:
    # Initialize the class and pick your pins for each LED
    def __init__(self, left_led=7, right_led=21):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(left_led, GPIO.OUT)
        GPIO.setup(right_led, GPIO.OUT)

    def run_left_side(self):
        GPIO.output(left_led, GPIO.HIGH)
        time.sleep(3)

    def run_right_side(self):
        GPIO.output(right_led, GPIO.HIGH)
        time.sleep(3)

    def run(self, side="both"):
        self.run_left_side()
        self.run_right_side()