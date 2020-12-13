import time
from adafruit_motorkit import MotorKit
from datetime import datetime

kit = MotorKit()

kit.motor1.throttle = -0.5
kit.motor2.throttle = 0.5

time.sleep(1)

kit.motor1.throttle = -0.4
kit.motor2.throttle = 0.4

time.sleep(4)
kit.motor1.throttle = 0
kit.motor2.throttle = 0