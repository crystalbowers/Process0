from seat_motor_control import Seat_MotorController
from steering_wheel_motor_control import Steering_Wheel_MotorController

# Running seat cushion
#seat_mc = Seat_MotorController(pwm_pin=32, pwm_freq=50)
#seat_mc.run(side="left", delay_secs=10)
#seat_mc.stop_motors()

# Running Steering Wheels
steering_wheel_mc = Steering_Wheel_MotorController(effect_num=118)
steering_wheel_mc.run()
