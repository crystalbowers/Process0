import busio
import board
#from adafruit_bus_device.i2c_device import I2CDevice
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C devices found:", [hex(i) for i in i2c.scan()])

address = 0x5A

if not address in i2c.scan():
    print("Could not find address")



























'''DEVICE_ADDRESS = 0x5A  # device address of DS3231 board
A_DEVICE_REGISTER = 0x0E  # device id register on the DS3231 board

# The follow is for I2C communications
comm_port = busio.I2C(board.SCL, board.SDA)
device = I2CDevice(comm_port, DEVICE_ADDRESS)

with device as bus_device:
    bus_device.write(bytes([A_DEVICE_REGISTER]))
    result = bytearray(1)
    bus_device.readinto(result)

print("".join("{:02x}".format(x) for x in result))'''