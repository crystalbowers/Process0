import Jetson.GPIO as GPIO
import time
import board
import busio
import adafruit_drv2605
import time


class Haptic_Controller:
	
	def _init_(self, pwm_pin1, pwm_pin2, motor_pin1, motor_pin2, motor_pin3, motor_pin4, pwm_freq, pwm_duty_cycle):

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

		# set the effect number
		self.effect_num = 118
		# Set motor side to be activated
		#        motor_selection = 0# 1 for (36, 38), -1 for (35, 37), 0 for both
		#
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

        # Initalize I2C buses (7 and 1) and DRV2065 modules
        # i2c1 and drv1 control the left side, while i2c2 and drv2 control the right side
		self.i2c1 = busio.I2C(board.SCL, board.SDA)
		self.i2c2 = busio.I2C(board.SCL_1, board.SDA_1)
		self.drv1 = adafruit_drv2605.DRV2605(self.i2c1, address=0x5A)
		self.drv2 = adafruit_drv2605.DRV2605(self.i2c2, address=0x5A)

        # Set effect number
		self.effect_num = effect_num

        # Set the sequence
		self.drv1.sequence[0] = adafruit_drv2605.Effect(self.effect_num)
		self.drv2.sequence[0] = adafruit_drv2605.Effect(self.effect_num)

        # Need to do this or else there's a 10 sec delay on motor every time
        # 10 sec delay will only occur once during initialization and not when it runs after that
		self.run_front_left_side(run_time=0)
		self.run_front_right_side(run_time=0)

	#change the effect number for front haptics
	def set_effect_num(num):
		self.effect_num = num;
		self.drv1.sequence[0] = adafruit_drv2605.Effect(self.effect_num)
		self.drv2.sequence[0] = adafruit_drv2605.Effect(self.effect_num)
		self.run_front_left_side(run_time=0)
		self.run_front_right_side(run_time=0)

	def run_front_left_side(self, run_time):
		self.drv1.play()
		time.sleep(run_time)
		self.drv1.stop()
		print("Front Left")

	def run_front_right_side(self, run_time):
		self.drv2.play()
		time.sleep(run_time)
		self.drv2.stop()
		print("Front Right")


	def run_back_left(self, run_time, motor_speed):

		set_motor_speed(0,motor_pin3,motor_pin4, pwm2)
		set_motor_speed(motor_speed,motor_pin1,motor_pin2, pwm1)
		time.sleep(durration)

		# Stop the motor
		set_motor_speed(0,motor_pin1,motor_pin2, pwm1)
		print("Back Left")
	
	def run_back_right(self, run_time, motor_speed):

		set_motor_speed(0,motor_pin1,motor_pin2, pwm1)
		set_motor_speed(motor_speed,motor_pin3,motor_pin4, pwm2)
		time.sleep(durration)

		# Stop the motor
		set_motor_speed(0,motor_pin3,motor_pin4, pwm2)
		print("Back Right")	


# Function to set the speed and direction of the motor
	def set_motor_speed(speed, motor_pin_1, motor_pin_2, pwm):
    # Set the direction of the motor
		if speed >= 0:
			GPIO.output(motor_pin_1, motor_direction)
			GPIO.output(motor_pin_2, not motor_direction)
		else:
			GPIO.output(motor_pin_1, not motor_direction)
			GPIO.output(motor_pin_2, motor_direction)
    # Set the duty cycle of the PWM
		self.pwm_duty_cycle = abs(speed)
		pwm.ChangeDutyCycle(pwm_duty_cycle)
		print("Spinning")

    def clean_up(self):
        # Cleanup GPIO pins
        self.pwm1.stop()
        self.pwm2.stop()
        GPIO.cleanup()


    if __name__ == "__main__":
    	Haptic = Haptic_Controller()
    	Haptic.run_front_left_side(5)
    	Haptic.clean_up()



