import sys
sys.path.append('../')

import encoder.encoder as encoder
import RPi.GPIO as GPIO
from time import sleep, time_ns
from adafruit_motorkit import MotorKit

value = 0



 

TARGET = 200
SAMPLETIME = 0.1
KP = 0.002
KD = 0.0002
KI=0
#KD = 0.0004
#KI = 0.001


kit = MotorKit()

e1 = encoder.Encoder(17)
e2 = encoder.Encoder(18)

m1_speed = 0
m2_speed = 0

e1_prev_error = 0
e2_prev_error = 0

e1_integral = 0
e2_integral =0

print("KP ; {} ; KI ; {} ; KD ;{}" .format(KP, KI, KD))

kit.motor1.throttle = m1_speed
kit.motor2.throttle = m2_speed

prev_time = time_ns()

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
    #print("m1 {} m2 {}".format(m1_speed, m2_speed))
        
    
    e1.reset()
    e2.reset()

    e1_prev_error = e1_error
    e2_prev_error = e2_error
    prev_time = curr_time

    sleep(SAMPLETIME)


