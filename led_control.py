import Jetson.GPIO as GPIO
import time

class LED_Controller:
    def __init__(self):
        left_led = 7
        right_led = 21
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(left_led, GPIO.OUT)
        GPIO.setup(right_led, GPIO.OUT)
        x = 1
        while x < 5:
            time.sleep(2)
            GPIO.output(left_led, GPIO.HIGH)
            GPIO.output(right_led, GPIO.HIGH)
            print("LED IS ON")
            time.sleep(2)
            GPIO.output(left_led, GPIO.LOW)
            GPIO.output(right_led, GPIO.LOW)
            print("LED IS OFF")
            x += 1
            print(x)
'''class LED_Controller:
    # Initialize the class and pick your pins for each LED
    def __init__(self, left_led=7, right_led=21):
        self.left_led = left_led
        self.right_led = right_led

        # Set up the board
        GPIO.setmode(GPIO.BOARD)

        # Set up the pins
        GPIO.setup(self.left_led, GPIO.OUT)
        GPIO.setup(self.right_led, GPIO.OUT)


    def run_left_side(self):
        GPIO.output(self.left_led, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(self.left_led, GPIO.LOW)

    def run_right_side(self):
        GPIO.output(self.right_led, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(self.right_led, GPIO.LOW)

    def run(self, side="both"):
        if side == "left":
            self.run_left_side()
        elif side == "right":
            self.run_right_side()
        elif side == "both":
            self.run_left_side()
            self.run_right_side()

    def clean_up(self):
        # Cleanup GPIO pins
        #self.left_led.stop()
        #self.right_led.stop()
        GPIO.cleanup()'''