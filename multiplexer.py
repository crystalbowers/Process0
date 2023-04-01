import board
import busio
import adafruit_tca9548a
import adafruit_drv2605
import time

effect_num = 118
run_time = 5

# Create I2C bus as normal
i2c = busio.I2C(board.SCL, board.SDA)
# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# For each motor driver, create it using the TCA9548A channel instead of the I2C object
#tsl1 = adafruit_drv2605.DRV2605(tca[7])
tsl2 = adafruit_drv2605.DRV2605(tca[4])

#tsl1.sequence[0] = adafruit_drv2605.Effect(effect_num)
tsl2.sequence[0] = adafruit_drv2605.Effect(effect_num)

'''tsl1.play()
time.sleep(run_time)
tsl1.stop()'''

tsl2.play()
time.sleep(run_time)
tsl2.stop()

