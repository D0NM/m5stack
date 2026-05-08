# RoverC-Pro

This Hat isn't supported in [UIFlow2 IDE](https://uiflow2.m5stack.com/) so, I added a driver wrapper and a custom block for UIFlow2

## HOW TO USE
1. Add **roverc_pro.py** into UIFlow2 with project files menu.
2. Add **roverc.m5b2** custom block into UIFlow2 project.
3. Add hardware **block I2C** and **init** it with proper **SCL** and **SDA pins** and freq (100K by default).
4. Add **Init RoverC block** with proper **i2c** bus.

## HINT
You may use **RoverC** with any controller with **i2c** bus.

### TODO
1. Clean these files from debug prints.
2. Servos block hasn't been tested yet.

[RoverC-PRO Docs](https://docs.m5stack.com/en/hat/hat_roverc_pro)