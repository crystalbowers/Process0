import Jetson.GPIO as GPIO
import time

class Seat_MotorController:
    def __init__(self, pwm_pin1=18, pwm_pin2=15, motor1_in1=36, motor1_in2=38, motor2_in3=35, motor2_in4=37,
                 pwm_freq=50, pwm_duty_cycle=0):

        # Set the GPIO pin for PWM output
        self.pwm_pin1 = pwm_pin1
        self.pwm_pin2 = pwm_pin2

        # Set the GPIO pins for motor control
        self.motor1_in1 = motor1_in1
        self.motor1_in2 = motor1_in2

        self.motor2_in3 = motor2_in3
        self.motor2_in4 = motor2_in4

        # Set the PWM frequency and duty cycle
        self.pwm_freq = pwm_freq
        self.pwm_duty_cycle = pwm_duty_cycle
        print("pwm dc",pwm_duty_cycle)

        # Set board
        GPIO.setmode(GPIO.BOARD)

        # Initialize the GPIO pins
        GPIO.setup(self.pwm_pin1, GPIO.OUT)
        GPIO.setup(self.motor1_in1, GPIO.OUT)
        GPIO.setup(self.motor1_in2, GPIO.OUT)

        GPIO.setup(self.pwm_pin2, GPIO.OUT)
        GPIO.setup(self.motor2_in3, GPIO.OUT)
        GPIO.setup(self.motor2_in4, GPIO.OUT)

        # Create PWM instance
        self.pwm1 = GPIO.PWM(self.pwm_pin1, self.pwm_freq)
        self.pwm2 = GPIO.PWM(self.pwm_pin2, self.pwm_freq)

        # Start PWM with duty cycle of 0
        self.pwm1.start(self.pwm_duty_cycle)
        self.pwm2.start(self.pwm_duty_cycle)
        print("self dc:",self.pwm_duty_cycle)

    def set_duty_cycle(self, duty_cycle):
        self.pwm_duty_cycle = duty_cycle
        self.pwm1.ChangeDutyCycle(self.pwm_duty_cycle)
        self.pwm2.ChangeDutyCycle(self.pwm_duty_cycle)
        print("oop")

    def set_motor_duty_cycle(self, duty_cycle, motor_pin_a, motor_pin_b):
        # motor pin a is 1 or 3
        # motor pin b is 2 or 4
        # Set the direction of the motor
        # forward
        if duty_cycle >= 0:
            GPIO.output(motor_pin_a, GPIO.HIGH)
            GPIO.output(motor_pin_b, GPIO.LOW)
            print("yup")
        else:
            # backward
            GPIO.output(motor_pin_a, GPIO.LOW)
            GPIO.output(motor_pin_b, GPIO.HIGH)
            print("nope")
        # Set the duty cycle of the PWM
        self.set_duty_cycle(abs(duty_cycle))
        print("new dc",duty_cycle)
        print("Spinning")

    def run_left_side(self, duty_cycle):
        self.set_motor_duty_cycle(duty_cycle, self.motor1_in1, self.motor1_in2)
        print("dance")

    def run_right_side(self, duty_cycle):
        self.set_motor_duty_cycle(duty_cycle, self.motor2_in3, self.motor2_in4)
        print("sing")

    def run(self, side="both", delay_secs=5, duty_cycle=50):
        print("I am in the run fn and my dc is", duty_cycle)
        if side == "left":
            self.run_left_side(duty_cycle)
            print("I ran left side")
        elif side == "right":
            self.run_right_side(duty_cycle)
            print("I ran right side")
        elif side == "both":
            self.run_left_side(duty_cycle)
            self.run_right_side(duty_cycle)
            print("I ran both sides")

        # wait for the given amount of time
        time.sleep(delay_secs)

        # stop the motors
        self.stop_motors()
        self.clean_up()

    def stop_motors(self):
        # set functions in the class using self (crystal note)
        self.set_duty_cycle(0)

    def clean_up(self):
        # Cleanup GPIO pins
        self.pwm1.stop()
        self.pwm2.stop()
        GPIO.cleanup()

    if __name__ == "__main__":
        # test if it works
        run()
        clean_up()