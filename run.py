# NOTE: RIGHT NOW SEAT MOTOR CONTROL AND STEERING WHEEL CLASSES EACH TRY TO SET UP GPIO BOARD.
# Comment out the one you dont want if running both.
#from seat_motor_control import Seat_MotorController
from orin_seat import Seat_MotorController
#from steering_wheel_motor_control import Steering_Wheel_MotorController
#from multiplexer_steering_code import Steering_Wheel_MotorController
#from led_control import LED_Controller
# Running seat cushion
seat_mc = Seat_MotorController()
seat_mc.run(side="right")
seat_mc.stop_motors()
seat_mc.clean_up()

# Running Steering Wheel Motors
#steering_wheel_mc = Steering_Wheel_MotorController(effect_num=118)
#steering_wheel_mc.run()
#print("I ran")

# Running LED lights
#steering_wheel_lc = LED_Controller()
#steering_wheel_lc.run(side="right")
#steering_wheel_lc.run(side="left")
#steering_wheel_lc.clean_up()
