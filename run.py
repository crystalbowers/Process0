# NOTE: RIGHT NOW SEAT MOTOR CONTROL AND STEERING WHEEL CLASSES EACH TRY TO SET UP GPIO BOARD.
# Comment out the one you dont want if running both.
#from seat_motor_control import Seat_MotorController
#from orin_seat import Seat_MotorController
from steering_wheel_motor_control import Steering_Wheel_MotorController

# Running seat cushion
#seat_mc = Seat_MotorController()
#seat_mc.run(side="left")

# Running Steering Wheel Motors
steering_wheel_mc = Steering_Wheel_MotorController(effect_num=118)
steering_wheel_mc.run()
print("I ran")

