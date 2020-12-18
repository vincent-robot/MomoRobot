import time
from adafruit_motorkit import MotorKit
from datetime import datetime


class Robot:
    def __init__(self):
        self.kit = MotorKit()

    def set_ordre_moteur(self,  gauche, droite):
        #print('[Robot - Commande moteur] - : Droite = ' + str(gauche) + " + Gauche = " + str(droite))

        
        
        self.kit.motor1.throttle = -droite * 0.7
        self.kit.motor2.throttle = gauche * 0.7

    def vector_to_differential(self, nJoyX, nJoyY):
        # CONFIG
        # - fPivYLimit : The threshold at which the pivot action starts
        #                This threshold is measured in units on the Y-axis
        #                away from the X-axis (Y=0). A greater value will assign
        #                more of the joystick's range to pivot actions.
        #                Allowable range: (0..+100)
        fPivYLimit = 37

        # TEMP VARIABLES
        nMotPremixL = 0 # Motor (left)  premixed output        (-128..+127)
        nMotPremixR = 0 # Motor (right) premixed output        (-128..+127)
        nPivSpeed = 0   # Pivot Speed                          (-128..+127)
        fPivScale = 0.0 # Balance scale b/w drive and pivot    (   0..1   )

        # Put to 0 if within the dead zone
        if nJoyX < 10 and nJoyY < 10:
            nJoyY = 0
            nJoyY = 0

        # Calculate Drive Turn output due to Joystick X input
        if(nJoyY>=0):
            # Forward
            nMotPremixL = 100 if nJoyX>=0 else 100.0 + nJoyX
            nMotPremixR = 100 - nJoyX if nJoyX>=0 else 100
        else:
            # Reverse
            nMotPremixR = 100 - nJoyX if nJoyX>=0 else 100
            nMotPremixL = 100 if nJoyX>=0 else 100 + nJoyX

        # Scale Drive output due to Joystick Y input (throttle)
        nMotPremixL = nMotPremixL * nJoyY/100
        nMotPremixR = nMotPremixR * nJoyY/100

        # Now calculate pivot amount
        #  - Strength of pivot (nPivSpeed) based on Joystick X input
        #  - Blending of pivot vs drive (fPivScale) based on Joystick Y input
        nPivSpeed = nJoyX
        fPivScale = 0.0 if abs(nJoyY)>fPivYLimit else 1.0-abs(nJoyY)/fPivYLimit

        # Calculate final mix of Drive and Pivot
        nMotMixL = ((1.0-fPivScale)*nMotPremixL + fPivScale*( nPivSpeed))/100 # Motor (left)  mixed output           (-128..+127)
        nMotMixR = ((1.0-fPivScale)*nMotPremixR + fPivScale*(-nPivSpeed))/100 # Motor (right) mixed output           (-128..+127)

        if nMotMixR !=0 :
            print('[Robot - differential] - Commande moteur D G : ' + str(nMotMixR) + " " + str(nMotMixL))

        self.set_ordre_moteur(nMotMixL, nMotMixR)

  