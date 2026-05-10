# roverc_pro.py  RoverC.PRO driver 10-May-2026
from hardware import I2C
import time

class RoverC_Pro:
    I2C_ADDR = 0x38

    def __init__(self, i2c: I2C):
        self.i2c = i2c
        self._buf = bytearray(4)

    # ====================== Motor Control ======================
    def set_motor_speed(self, m1: int, m2: int, m3: int, m4: int):
        """
        Set speed for all 4 Mecanum wheels.
        Range: -127 ~ +127  (negative = reverse)
        """
        self._buf[0] = self._clamp(m1, -127, 127) & 0xFF
        self._buf[1] = self._clamp(m2, -127, 127) & 0xFF
        self._buf[2] = self._clamp(m3, -127, 127) & 0xFF
        self._buf[3] = self._clamp(m4, -127, 127) & 0xFF
        self.i2c.writeto(self.I2C_ADDR, b'\x00' + self._buf[:4])

    def stop(self):
        """Stop all motors"""
        self.set_motor_speed(0, 0, 0, 0)

    # ====================== Simple Movement ======================
    def move_forward(self, speed: int = 80):
        self.set_motor_speed(speed, speed, speed, speed)

    def move_backward(self, speed: int = 80):
        self.set_motor_speed(-speed, -speed, -speed, -speed)

    def move_left(self, speed: int = 80):
        self.set_motor_speed(-speed, speed, speed, -speed)

    def move_right(self, speed: int = 80):
        self.set_motor_speed(speed, -speed, -speed, speed)

    def rotate_left(self, speed: int = 80):
        self.set_motor_speed(-speed, speed, -speed, speed)

    def rotate_right(self, speed: int = 80):
        self.set_motor_speed(speed, -speed, speed, -speed)

    # ====================== Servo Control ======================
    def set_servo_angle(self, servo1: int = 90, servo2: int = 90):
        """
        Set servo angles (0~180�)
        servo1 and servo2 are the two expansion servos on RoverC-Pro
        """
        self._buf[0] = self._clamp(servo1, 0, 180)
        self._buf[1] = self._clamp(servo2, 0, 180)
        self.i2c.writeto(self.I2C_ADDR, b'\x10' + self._buf[:2])

    # ====================== Helper ======================
    def _clamp(self, value, min_val, max_val):
        return max(min_val, min(max_val, value))

    def scan(self):
        """Scan I2C bus"""
        return self.i2c.scan()
