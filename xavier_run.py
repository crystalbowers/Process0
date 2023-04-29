from xavier_seat_motor_control import Seat_MotorController
from xavier_steering_wheel_motor_control import Steering_Wheel_MotorController

# There are three board types: 1) Empty string 2) I2C (means it's set up for the steering wheel)
# 3) PWM (means it's set up for the seat cushion)
board_type = ""

# Running seat cushion
if board_type == "" or "I2C":
    seat_mc = Seat_MotorController()
    board_type = "PWM"
    seat_mc.run(side="left")
    print("I ran seat cushion")

# Running Steering Wheel Motors
if board_type == "PWM":
    steering_wheel_mc = Steering_Wheel_MotorController(effect_num=118)
    board_type = "I2C"
    steering_wheel_mc.run()
    print("I ran steering wheel")

##########################
board_type = ""

# if direction is from backwards

# Running seat cushion
if board_type == "" or "I2C":
    from xavier_seat_motor_control import Seat_MotorController
    seat_mc = Seat_MotorController()

    # if direction back left:
    seat_mc.run(side="left")
    print("I ran left seat cushion")

    # if direction back right
    seat_mc.run(side="right")
    print("I ran right seat cushion")

    # Change board type to PWM
    board_type = "PWM"

elif board_type == "PWM":
    # if direction back left:
    seat_mc.run(side="left")
    print("I ran left seat cushion")

    # if direction back right
    seat_mc.run(side="right")
    print("I ran right seat cushion")

    # Board type stays as PWM

# if direction is from front
# Running Steering Wheel Motors
if board_type == "PWM" or "":
    from xavier_steering_wheel_motor_control import Steering_Wheel_MotorController
    steering_wheel_mc = Steering_Wheel_MotorController(effect_num=118)

    # if direction front left:
    steering_wheel_mc.run(side="left")
    print("I ran left steering wheel")

    # if direction front right:
    steering_wheel_mc.run(side="right")
    print("I ran right steering wheel")

    # Change board type variable to I2C
    board_type = "I2C"

elif board_type == "I2C"
    # if direction front left:
    steering_wheel_mc.run(side="left")
    print("I ran left steering wheel")

    # if direction front right:
    steering_wheel_mc.run(side="right")
    print("I ran right steering wheel")

    # Board will remain as I2C