import i2c_bus
from roverc_pro import RoverC_Pro
import time

# Initialize I2C (recommended way)
i2c = i2c_bus.easyI2C(i2c_bus.PORTA, RoverC_Pro.I2C_ADDR)

rover = RoverC_Pro(i2c)

rover.stop()
time.sleep(1)

print("Moving forward...")
rover.move_forward(100)
time.sleep(2)

print("Moving right...")
rover.move_right(80)
time.sleep(2)

print("Rotating left...")
rover.rotate_left(70)
time.sleep(2)

rover.stop()
print("Stopped")