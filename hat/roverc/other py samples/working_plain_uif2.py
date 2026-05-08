import os, sys, io
import M5
from M5 import *
from hardware import Pin
from hardware import I2C

# import i2c_bus
from roverc_pro import RoverC_Pro

i2c0 = None


def setup():
  global i2c0

  M5.begin()
  Widgets.setRotation(0)
  Widgets.fillScreen(0x247255)

  i2c0 = I2C(0, scl=Pin(26), sda=Pin(0), freq=100000)
  rover = RoverC_Pro(i2c0)
  print(i2c0.scan())
  print(rover.scan())
  print("--")

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


def loop():
  global i2c0
  M5.update()


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
