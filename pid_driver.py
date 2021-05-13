import time
import math
import encoder.encoder as encoder
from datetime import datetime
from adafruit_motorkit import MotorKit

class pid_driver:
    def __init__(self):
        self.kit = MotorKit()
        self.m1_speed = 0
        self.m2_speed = 0       
    
    def set(_self, request_left, request_right):
        prin("hello")



def PID_loop(kit):
    self.SAMPLETIME = 0.1
    self.KP = 0.002
    self.KD = 0.0002
    self.I=0

    self.e1 = encoder.Encoder(17)
    self.e2 = encoder.Encoder(18)

    self.e1_prev_error = 0
    self.e2_prev_error = 0

    self.e1_integral = 0
    self.e2_integral =0
   
    while True:
        e1_error = TARGET - e1.read()
        e2_error = TARGET - e2.read()

        curr_time = time_ns()
        dt = (curr_time - prev_time) / 1000000000

        e1_integral += e1_error * dt
        e2_integral += e2_error * dt 

        m1_speed += (e1_error * KP) + ((e1_error - e1_prev_error) * KD / dt) + e1_integral * KI 
        m2_speed += (e2_error * KP) + ((e2_error - e2_prev_error) * KD / dt) + e2_integral * KI 

        m1_speed = max(min(1, m1_speed), 0)
        m2_speed = max(min(1, m2_speed), 0)

        kit.motor1.throttle = m1_speed
        kit.motor2.throttle = m2_speed

        print("e1 ; {} ; e2 ; {} ; m1 ; {} ; m2 ; {} ; dt ; {}".format(e1.read(), e2.read(), m1_speed, m2_speed, dt))
    