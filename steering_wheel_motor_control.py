import board
import busio
import adafruit_drv2605
import time

class Steering_Wheel_MotorController:
    def __init__(self, effect_num=118):
        # Initalize I2C buses (7 and 1) and DRV2065 modules
        # i2c1 and drv1 control the left side, while i2c2 and drv2 control the right side
        self.i2c1 = busio.I2C(board.SCL, board.SDA)
        self.i2c2 = busio.I2C(board.SCL_1, board.SDA_1)
        self.drv1 = adafruit_drv2605.DRV2605(self.i2c1, address=0x5A)
        self.drv2 = adafruit_drv2605.DRV2605(self.i2c2, address=0x5A)

        # Set effect number
        self.effect_num = effect_num

        # Set the sequence
        self.drv1.sequence[0] = adafruit_drv2605.Effect(self.effect_num)
        self.drv2.sequence[0] = adafruit_drv2605.Effect(self.effect_num)

        # Need to do this or else there's a 10 sec delay on motor every time
        # 10 sec delay will only occur once during initialization and not when it runs after that
        self.run_left_side(run_time=0)
        self.run_right_side(run_time=0)

    def run_left_side(self, run_time=3):
        self.drv1.play()
        time.sleep(run_time)
        self.drv1.stop()

    def run_right_side(self,run_time=3):
        self.drv2.play()
        time.sleep(run_time)
        self.drv2.stop()

    def run_both_sides(self, run_time=3):
        self.drv1.play()
        time.sleep(run_time)
        self.drv1.stop()

        self.drv2.play()
        time.sleep(run_time)
        self.drv2.stop()
    def run(self,side="both",run_time=3):
        # Run for three seconds then stop
        if side == "both":
            self.run_both_sides(run_time)
        elif side == "left":
            self.run_left_side(run_time)
        elif side == "right":
            self.run_right_side(run_time)

if __name__ == "__main__":
    s = Steering_Wheel_MotorController()
    # test if it works
    s.run(run_time=1)
    time.sleep(4)
    s.run(run_time=5)
