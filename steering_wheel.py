import board
import busio
import adafruit_drv2605
import time

# Initalize I2C bus and DRV2065 module
i2c = busio.I2C(board.SCL, board.SDA)
drv = adafruit_drv2605.DRV2605(i2c)

# Run vibrations
effect_num = 118
drv.sequence[0] = adafruit_drv2605.Effect(effect_num)
#drv.sequence[1] = adafruit_drv2605.Pause(2)
#drv.sequence[2] = adafruit_drv2605.Effect(effect_num)
#drv.sequence[3] = adafruit_drv2605.Effect(0)
drv.play()
time.sleep(5)
drv.stop()

print("Those two effects with pauses")

#drv.stop()

# We like 83. 106 is better, slightly stronger than 82
# 70 is wierd
# 118 is strongest but won't stop

# Wiring Info:
# sda 3
# scl 5
# ground ground
# bus 1

