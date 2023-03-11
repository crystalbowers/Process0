import board
import busio
import adafruit_drv2605
i2c = busio.I2C(board.SCL, board.SDA)
drv = adafruit_drv2605.DRV2605(i2c)

drv.sequence[0] = adafruit_drv2605.Effect(1)
print("sharp click")

drv.play()
drv.sequence[0] = adafruit_drv2605.Effect(47)
drv.play()
print("strong buzz")

drv.sequence[0] = adafruit_drv2605.Effect(1)
drv.sequence[1] = adafruit_drv2605.Pause(0.5)
drv.sequence[2] = adafruit_drv2605.Effect(47)
drv.sequence[3] = adafruit_drv2605.Effect(0)
drv.play()
print("Those two effects with pauses")
drv.stop()