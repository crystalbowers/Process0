import Jetson.GPIO as GPIO
import time

# Set the GPIO pin for PWM output
pwm_pin = 32

# Set the GPIO pins for motor control
motor_pin1 = 36
motor_pin2 = 38
# Set the PWM frequency and duty cycle
pwm_freq = 50
pwm_duty_cycle = 10

# Set the direction of the motor
motor_direction = 1  # 1 for forward, -1 for backward

GPIO.setmode(GPIO.BOARD)

# Initialize the GPIO pins
GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.setup(motor_pin1, GPIO.OUT)
GPIO.setup(motor_pin2, GPIO.OUT)

# Create PWM instance
pwm = GPIO.PWM(pwm_pin, pwm_freq)

# Start PWM with duty cycle of 0
pwm.start(pwm_duty_cycle)

# Function to set the speed and direction of the motor
def set_motor_speed(speed):
    global pwm_duty_cycle
    global motor_direction
    # Set the direction of the motor
    if speed >= 0:
        GPIO.output(motor_pin1, motor_direction)
        GPIO.output(motor_pin2, not motor_direction)
    else:
        GPIO.output(motor_pin1, not motor_direction)
        GPIO.output(motor_pin2, motor_direction)
    # Set the duty cycle of the PWM
    pwm_duty_cycle = abs(speed)
    pwm.ChangeDutyCycle(pwm_duty_cycle)

# Example usage: set the speed to 50%
set_motor_speed(50)

# Wait for 5 seconds
time.sleep(5)

# Stop the motor
set_motor_speed(0)

# Cleanup GPIO pins
pwm.stop()
GPIO.cleanup()
