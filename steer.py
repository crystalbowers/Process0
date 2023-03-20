import board
import busio
import adafruit_drv2605
import time
i2c = busio.I2C(board.SCL, board.SDA)
drv = adafruit_drv2605.DRV2605(i2c)

# Start real-time playback
drv.realtime_value = 64
print("drv real time value:",drv.realtime_value)
drv.mode = adafruit_drv2605.MODE_REALTIME
print("mode is",drv.mode)

# Buzz the motor briefly at 50% and 100% amplitude
print("drv real time value:",drv.realtime_value)
drv.realtime_value = 64
print("please run")
time.sleep(2)
drv.realtime_value = 127
print("drv real time value:",drv.realtime_value)
print("did i go")
time.sleep(3)

# Stop real-time playback
drv.realtime_value = 0
print("drv real time value:",drv.realtime_value)
drv.mode = adafruit_drv2605.MODE_INTTRIG
print("mode is",drv.mode)



