import board
import busio
import adafruit_tca9548a
import adafruit_drv2605
import time

class Steering_Wheel_MotorController:
    def __init__(self, effect_num=118):
        # Initalize I2C bus and DRV2065 module
        self.i2c = busio.I2C(board.SCL, board.SDA)
        #self.drv = adafruit_drv2605.DRV2605(self.i2c)

        # Create the TCA9548A object and give it the I2C bus
        self.tca = adafruit_tca9548a.TCA9548A(i2c)

        # For each motor driver, create it using the TCA9548A channel instead of the I2C object
        self.tsl1 = adafruit_drv2605.DRV2605(tca[0])
        self.tsl2 = adafruit_drv2605.DRV2605(tca[1])

        # Set effect number
        self.effect_num = effect_num

        # Set the sequence
        #self.drv.sequence[0] = adafruit_drv2605.Effect(self.effect_num)
        self.tsl1.sequence[0] = adafruit_drv2605.Effect(effect_num)
        self.tsl2.sequence[0] = adafruit_drv2605.Effect(effect_num)

        # Need to do this or else there's a 10 sec delay on motor every time
        # 10 sec delay will only occur once during initialization and not when it runs after that
        self.run_left_side(run_time=0)
        self.run_right_side(run_time=0)

    def run_left_side(self, run_time=5):
        tsl1.play()
        time.sleep(run_time)
        tsl1.stop()

    def run_right_side(self,run_time=5):
        tsl2.play()
        time.sleep(run_time)
        tsl2.stop()

    def run(self,side="left",run_time=5):
        # Run for five seconds then stop
        if side == "left":
            self.run_left_side(run_time)
        elif side =="right":
            self.run_right_side(run_time)

if __name__ == "__main__":
    s = Steering_Wheel_MotorController()
    # test if it works
    s.run(run_time=1)
    time.sleep(4)
    s.run(run_time=5)


