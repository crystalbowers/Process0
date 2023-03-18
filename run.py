from seat_motor_control import Seat_MotorController
from steering_wheel_motor_control import Steering_Wheel_MotorController
from led_control import LED_Controller
# Running seat cushion
#seat_mc = Seat_MotorController()
#seat_mc.run(side="left", delay_secs=10)
#seat_mc.stop_motors()

# Running Steering Wheels
#steering_wheel_mc = Steering_Wheel_MotorController(effect_num=118)
#steering_wheel_mc.run()

steering_wheel_lc = LED_Controller()
steering_wheel_lc.run(side="left")
steering_wheel_lc.clean_up()
