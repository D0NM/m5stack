import os, sys, io
import M5
from M5 import *
from hardware import Pin
from hardware import I2C
import time



i2c1 = None


def setup():
  global i2c1

  M5.begin()
  Widgets.setRotation(0)
  Widgets.fillScreen(0x247255)

  i2c1 = I2C(1, scl=Pin(26), sda=Pin(0), freq=100000)
  time.sleep(1)
  print(i2c1.scan())


def loop():
  global i2c1
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
