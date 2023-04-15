import Jetson.GPIO as GPIO
import time

class Seat_MotorController:
    def __init__(self):
        # Set the GPIO pin for PWM output
        self.pwm_pin1 = 18
        self.pwm_pin2 = 15

        # Set the GPIO pins for motor control
        self.motor_pin1 = 36
        self.motor_pin2 = 38

        self.motor_pin3 = 35
        self.motor_pin4 = 37

        # Set the PWM frequency and duty cycle
        self.pwm_freq = 50
        self.pwm_duty_cycle = 0

        # Set motor side to be activated
        #self.motor_selection = -1 # 1 for (36, 38), -1 for (35, 37), 0 for both

        # Set the direction of the motor
        self.motor_direction = 1  # 1 for forward, -1 for backward

        GPIO.setmode(GPIO.BOARD)

        # Initialize the GPIO pins
        GPIO.setup(self.pwm_pin1, GPIO.OUT)
        GPIO.setup(self.motor_pin1, GPIO.OUT)
        GPIO.setup(self.motor_pin2, GPIO.OUT)

        GPIO.setup(self.pwm_pin2, GPIO.OUT)
        GPIO.setup(self.motor_pin3, GPIO.OUT)
        GPIO.setup(self.motor_pin4, GPIO.OUT)

        # Create PWM instance
        self.pwm1 = GPIO.PWM(self.pwm_pin1, self.pwm_freq)
        self.pwm2 = GPIO.PWM(self.pwm_pin2, self.pwm_freq)

        # Start PWM with duty cycle of 0
        self.pwm1.start(self.pwm_duty_cycle)
        self.pwm2.start(self.pwm_duty_cycle)

    # Function to set the speed and direction of the motor
    def set_motor_duty(self, duty, motor_pin_a, motor_pin_b, pwm):
        #global pwm_duty_cycle
        #global motor_direction
        # Set the direction of the motor
        if duty >= 0:
            GPIO.output(motor_pin_a, self.motor_direction)
            GPIO.output(motor_pin_b, not self.motor_direction)
        else:
            GPIO.output(motor_pin_a, not self.motor_direction)
            GPIO.output(motor_pin_b, self.motor_direction)
        # Set the duty cycle of the PWM
        self.pwm_duty_cycle = abs(duty)
        pwm.ChangeDutyCycle(self.pwm_duty_cycle)
        print("Spinning")

    def run(self, side):
        # Run both motors
        if side=="both":
            self.set_motor_duty(50, self.motor_pin1, self.motor_pin2, self.pwm1)
            self.set_motor_duty(50, self.motor_pin3, self.motor_pin4, self.pwm2)

            # Wait for 5 seconds
            time.sleep(3)

            # Stop the motor
            self.set_motor_duty(0, self.motor_pin1, self.motor_pin2, self.pwm1)
            self.set_motor_duty(0, self.motor_pin3, self.motor_pin4, self.pwm2)
            print("both")

        # Run left motor
        elif side == "left":
            self.set_motor_duty(50, self.motor_pin1, self.motor_pin2, self.pwm1)

            # Wait for 5 seconds
            time.sleep(3)

            # Stop the motor
            self.set_motor_duty(0, self.motor_pin1, self.motor_pin2, self.pwm1)
            print("left")

        # Run right motor
        elif side == "right":
            self.set_motor_duty(70, self.motor_pin3, self.motor_pin4, self.pwm2)

            # Wait for 5 seconds
            time.sleep(3)

            # Stop the motor
            self.set_motor_duty(0, self.motor_pin3, self.motor_pin4, self.pwm2)
            print("right")

        # Cleanup GPIO pins
        self.pwm1.stop()
        self.pwm2.stop()
        GPIO.cleanup()
        print("cleaned up")