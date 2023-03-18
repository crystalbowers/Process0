import Jetson.GPIO as GPIO
import time
left_led=7
right_led=21
GPIO.setmode(GPIO.BOARD)
GPIO.setup(left_led, GPIO.OUT)
GPIO.setup(right_led, GPIO.OUT)
x=1
while x<5:
        time.sleep(2)
        GPIO.output(left_led, GPIO.HIGH)
        GPIO.output(right_led, GPIO.HIGH)
        print("LED IS ON")
        time.sleep(2)
        GPIO.output(left_led, GPIO.LOW)
        GPIO.output(right_led, GPIO.LOW)
        print("LED IS OFF")
        x+=1
        print(x)