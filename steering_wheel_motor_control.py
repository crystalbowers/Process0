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

    def run(self,run_time=5):
        # Run vibrations
        self.drv.sequence[0] = adafruit_drv2605.Effect(self.effect_num)

        # Run for five seconds then stop
        self.drv.play()
        time.sleep(run_time)
        self.drv.stop()

    if __name__ == "__main__":
        # test if it works
        run()
