import sys
sys.path.append('../')

import encoder.encoder as encoder
from time import sleep
from adafruit_motorkit import MotorKit


value = 0




SAMPLETIME = 0.1

kit = MotorKit()

motor1encoder = encoder.Encoder(17)
motor2encoder = encoder.Encoder(18)


#find a sample rate
while True:
    kit.motor1.throttle = 1
    kit.motor2.throttle = 1

        
    print("e1 %s e2 %s" %(motor1encoder.read(), motor2encoder.read()))
    motor1encoder.reset()
    motor2encoder.reset()
    
    sleep(SAMPLETIME)


