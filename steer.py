import board
import busio
import adafruit_drv2605
import time
i2c = busio.I2C(board.SCL, board.SDA)
drv = adafruit_drv2605.DRV2605(i2c)
drv.realtime_value = 100
drv.mode = adafruit_drv2605.MODE_REALTIME
print("set mode")
# Buzz the motor briefly at 50% and 100% amplitude
drv.realtime_value = 100
print("ran 2")
'''
# Buzz the motor briefly at 50% and 100% amplitude
drv.realtime_value = 64
time.sleep(0.5)
drv.realtime_value = 127
time.sleep(0.5)
print("I ran with new code")


effect_num = 118
run_time = 5
# Run vibrations
drv.sequence[0] = adafruit_drv2605.Effect(effect_num)

# Run for five seconds then stop
drv.play()
time.sleep(run_time)
drv.stop()'''



# Stop real-time playback
#drv.realtime_value = 0
#drv.mode = adafruit_drv2605.MODE_INTTRIG
