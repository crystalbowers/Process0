import board
import busio
import adafruit_drv2605
import time


class Steering_Wheel_Motor_Controller:
    def __init__(self, effect_num=118, scl=board.SCL, sda=board.SDA):
        # Initalize I2C buses and DRV2065 modules
        self.i2c = busio.I2C(scl, sda)

        self.drv = adafruit_drv2605.DRV2605(self.i2c, address=0x5A)

        # Set effect number
        self.effect_num = effect_num

        # Set the sequence
        self.drv.sequence[0] = adafruit_drv2605.Effect(self.effect_num)

        # Need to do this or else there's a 10 sec delay on motor every time
        # 10 sec delay will only occur once during initialization and not when it runs after that
        self.run(run_time=0)

    def run(self, run_time=5):
        # Run for five seconds then stop
        self.drv.play()
        time.sleep(run_time)
        self.drv.stop()


if __name__ == "__main__":
    # left controller uses default i2c bus
    left_controller = Steering_Wheel_Motor_Controller()

    # specify special i2c bus for right controller
    right_controller = Steering_Wheel_Motor_Controller(scl=board.SCL_1, sda=board.SDA_1)

    # run the left controller
    left_controller.run(run_time=1)
    time.sleep(2)

    # run the right controller
    right_controller.run(run_time=1)