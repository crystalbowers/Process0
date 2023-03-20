from steering_wheel_motor_control import Steering_Wheel_MotorController

steering_wheel_mc = Steering_Wheel_MotorController(effect_num=118)
# Running Steering Wheel Motors
for i in range(4):
    steering_wheel_mc.run()
    print("I ran", i)
