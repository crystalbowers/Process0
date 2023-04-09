# NOTE: RIGHT NOW SEAT MOTOR CONTROL AND STEERING WHEEL CLASSES EACH TRY TO SET UP GPIO BOARD.
# Comment out the one you dont want if running both.
from seat_motor_control import Seat_MotorController
#from steering_wheel_motor_control import Steering_Wheel_MotorController
#from multiplexer_steering_code import Steering_Wheel_MotorController

# Running seat cushion
seat_mc = Seat_MotorController()

# if current amplitude bigger than old amplitude and old classification = siren and current classification=siren:
    seat_mc.run(side="both", delay_secs=3, duty_cycle=60)

# if current amplitude bigger than old amplitude and old classification = siren and current classification=siren and the
#older classification:
    seat_mc.run(side="both", delay_secs=3, duty_cycle=70)

#else:
    seat_mc.run(side="both", delay_secs=3, duty_cycle=50)

seat_mc.stop_motors()
seat_mc.clean_up()



# Running Steering Wheel Motors

# if current amplitude bigger than old amplitude and old classification = siren and current classification=siren:
steering_wheel_mc = Steering_Wheel_MotorController(effect_num=106)

# if current amplitude bigger than old amplitude and old classification = siren and current classification=siren and the
#older classification:
steering_wheel_mc = Steering_Wheel_MotorController(effect_num=118)

else:
    steering_wheel_mc = Steering_Wheel_MotorController(effect_num=83)

steering_wheel_mc.run()





