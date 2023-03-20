import board
import busio
import adafruit_drv2605
import time

class Steering_Wheel_MotorController:
    def __init__(self, effect_num=118):
        # Initalize I2C bus and DRV2065 module
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.drv = adafruit_drv2605.DRV2605(self.i2c)

        # Set effect number
        self.effect_num = effect_num

        # Set the sequence
        self.drv.sequence[0] = adafruit_drv2605.Effect(self.effect_num)

        # Need to do this or else there's a 10 sec delay on motor every time
        # 10 sec delay will only occur once during initialization and not when it runs after that
        self.run(run_time=0)

    def run(self,run_time=5):
        # Run for five seconds then stop
        self.drv.play()
        time.sleep(run_time)
        self.drv.stop()

if __name__ == "__main__":
    s = Steering_Wheel_MotorController()
    # test if it works
    s.run(run_time=2)
    time.sleep(2)
    s.run()
