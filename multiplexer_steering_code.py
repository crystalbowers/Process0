import board
import busio
import adafruit_tca9548a
import adafruit_drv2605
import time

class Steering_Wheel_MotorController:
    def __init__(self, effect_num=118,channel_1=0,channel_2=1):
        # Initalize I2C bus and DRV2065 module
        self.i2c = busio.I2C(board.SCL, board.SDA)
        #self.drv = adafruit_drv2605.DRV2605(self.i2c)

        # Create the TCA9548A object and give it the I2C bus
        self.tca = adafruit_tca9548a.TCA9548A(self.i2c)

        # For each motor driver, create it using the TCA9548A channel instead of the I2C object
        self.tsl1 = adafruit_drv2605.DRV2605(self.tca[channel_1])
        self.tsl2 = adafruit_drv2605.DRV2605(self.tca[channel_2])

        # Set effect number
        self.effect_num = effect_num

        # Set the sequence for each motor driver connected to the multiplexer
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

    def run_both_sides(self, run_time=5):
        tsl1.play()
        tsl2.play()
        time.sleep(run_time)
        tsl1.stop()
        tsl2.stop()

    def run(self,side="both",run_time=5):
        # Run for five seconds then stop
        if side == "both":
            self.run_both_sides(run_time)
        elif side == "left":
            self.run_left_side(run_time)
        elif side =="right":
            self.run_right_side(run_time)

if __name__ == "__main__":
    s = Steering_Wheel_MotorController()
    # test if it works
    s.run(run_time=5)
    s.run(run_time=5)


