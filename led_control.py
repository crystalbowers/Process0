import Jetson.GPIO as GPIO
import time

class LED_Controller:
    # Initialize the class and pick your pins for each LED
    def __init__(self, left_led=7, right_led=21):
        self.left_led = left_led
        self.right_led = right_led

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.left_led, GPIO.OUT)
        GPIO.setup(self.right_led, GPIO.OUT)

    def run_left_side(self):
        GPIO.output(self.left_led, GPIO.HIGH)
        time.sleep(3)

    def run_right_side(self):
        GPIO.output(self.right_led, GPIO.HIGH)
        time.sleep(3)

    def run(self, side="both"):
        self.run_left_side()
        self.run_right_side()

    def clean_up(self):
        # Cleanup GPIO pins
        self.left_led.stop()
        self.right_led.stop()
        GPIO.cleanup()