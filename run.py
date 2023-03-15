from motor_control import MotorController

mc = MotorController(pwm_pin=32, pwm_freq=50)

mc.run(side="left", delay_secs=10)

mc.stop_motors()