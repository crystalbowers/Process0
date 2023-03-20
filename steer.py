import board
import busio
import adafruit_drv2605
import time
i2c = busio.I2C(board.SCL, board.SDA)
drv = adafruit_drv2605.DRV2605(i2c)
# Start real-time playback
drv.realtime_value = 0
drv.mode = adafruit_drv2605.MODE_REALTIME

# Buzz the motor briefly at 50% and 100% amplitude
drv.realtime_value = 64
time.sleep(0.5)
drv.realtime_value = 127
time.sleep(0.5)

# Stop real-time playback
drv.realtime_value = 0