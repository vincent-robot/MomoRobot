import time
import math
import threading
import logging
import encoder.encoder as encoder
from datetime import datetime
from adafruit_motorkit import MotorKit

class Chassis:
    def __init__(self):
        self.kit = MotorKit()
        self.roue_droite = Roue(self.kit, 1, 17)
        self.roue_gauche = Roue(self.kit, 2, 18)


class Roue:
    def __init__(self, kit, motor_channel, encoder_channel):
        self.consigne = 0
        self.encoder = encoder.Encoder(encoder_channel)

        if motor_channel == 1:
            self.motor = kit.motor1
        elif motor_channel == 2:
            self.motor = kit.motor2

        self.my_thread = threading.Thread(target=self.thread_motor, args=(motor_channel,), daemon=True)
        self.my_thread.start()
           
    def set_tension(self, vitesse):
        self.consigne = vitesse

    def thread_motor(self, name):
        self.KP = 0.002
        self.KD = 0.0002
        #self.KI=0
        self.sampletime = 0.1
        self.prev_error = 0
        self.prev_encoder = self.encoder.read()
        self.current_encoder = 0
        #self.integral = 0
        self.m_speed = 0
        self.prev_time = time.time_ns()
        
        while True:
            time.sleep(self.sampletime)
            self.current_encoder= self.encoder.read()
            curr_time = time.time_ns()
            dt = (curr_time - self.prev_time) / 1000000000
            self.vitesse = (self.current_encoder - self.prev_encoder)
            error = self.consigne - self.vitesse
            

           
            #self.integral += error * dt
            self.m_speed += (error * self.KP) + ((error - self.prev_error) * self.KD / dt) #+ self.integral * self.KI 
            self.m_speed = max(min(1, self.m_speed), 0)
            self.motor.throttle = self.m_speed     
            
            self.prev_error = error
            self.prev_encoder = self.current_encoder           
            self.prev_time = curr_time
            print("vitesse ; {} ; m ; {} ; dt ; {}".format(self.vitesse, self.m_speed, dt))
            


          
    
   
        
        

logging.basicConfig(level=logging.DEBUG)
chassis=Chassis()

"""for x in range(10, 30):
    chassis.roue_droite.consigne = x*10
    time.sleep(1)
"""

chassis.roue_gauche.consigne = -150
chassis.roue_droite.consigne = -150


time.sleep(10)


chassis.kit.motor1.throttle = 0
chassis.kit.motor2.throttle = 0
    
