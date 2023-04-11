import Jetson.GPIO as GPIO
import time

# Set the GPIO pin for PWM output
pwm_pin1 = 18
pwm_pin2 = 15

# Set the GPIO pins for motor control
motor_pin1 = 36
motor_pin2 = 38

motor_pin3 = 35
motor_pin4 = 37

# Set the PWM frequency and duty cycle
pwm_freq = 50
pwm_duty_cycle = 10

# Set motor side to be activated
motor_selection = -1 # 1 for (36, 38), -1 for (35, 37), 0 for both

# Set the direction of the motor
motor_direction = 1  # 1 for forward, -1 for backward

GPIO.setmode(GPIO.BOARD)

# Initialize the GPIO pins
GPIO.setup(pwm_pin1, GPIO.OUT)
GPIO.setup(motor_pin1, GPIO.OUT)
GPIO.setup(motor_pin2, GPIO.OUT)

GPIO.setup(pwm_pin2, GPIO.OUT)
GPIO.setup(motor_pin3, GPIO.OUT)
GPIO.setup(motor_pin4, GPIO.OUT)

# Create PWM instance
pwm1 = GPIO.PWM(pwm_pin1, pwm_freq)
pwm2 = GPIO.PWM(pwm_pin2, pwm_freq)

# Start PWM with duty cycle of 0
pwm1.start(pwm_duty_cycle)
pwm2.start(pwm_duty_cycle)

# Function to set the speed and direction of the motor
def set_motor_speed(speed, motor_pin_1, motor_pin_2, pwm):
    global pwm_duty_cycle
    global motor_direction
    # Set the direction of the motor
    if speed >= 0:
        GPIO.output(motor_pin_1, motor_direction)
        GPIO.output(motor_pin_2, not motor_direction)
    else:
        GPIO.output(motor_pin_1, not motor_direction)
        GPIO.output(motor_pin_2, motor_direction)
    # Set the duty cycle of the PWM
    pwm_duty_cycle = abs(speed)
    pwm.ChangeDutyCycle(pwm_duty_cycle)
    print("Spinning")

# Run both motors
if motor_selection==0:
    set_motor_speed(50,motor_pin1,motor_pin2, pwm1)
    set_motor_speed(50,motor_pin3,motor_pin4, pwm2)

    # Wait for 5 seconds
    time.sleep(5)

    # Stop the motor
    set_motor_speed(0,motor_pin1,motor_pin2, pwm1)
    set_motor_speed(0,motor_pin3,motor_pin4, pwm2)
    print("both")

# Run left motor
elif motor_selection == 1:
    set_motor_speed(50,motor_pin1,motor_pin2, pwm1)

    # Wait for 5 seconds
    time.sleep(5)

    # Stop the motor
    set_motor_speed(0,motor_pin1,motor_pin2, pwm1)
    print("left")

# Run right motor
elif motor_selection == -1:
    set_motor_speed(50, motor_pin3, motor_pin4, pwm2)

    # Wait for 5 seconds
    time.sleep(5)

    # Stop the motor
    set_motor_speed(0, motor_pin3, motor_pin4, pwm2)
    print("right")

# Cleanup GPIO pins
pwm1.stop()
pwm2.stop()
GPIO.cleanup()
