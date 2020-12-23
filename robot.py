import time
import math
from datetime import datetime
from adafruit_motorkit import MotorKit



class Robot:
    def __init__(self):
        self.kit = MotorKit()

    def set_ordre_moteur(self,  gauche, droite):
        """ Send order to motor accouding to methos input

        Keyword arguments:
        gauche : throtlle moteur gauche (-1..1)
        droite : throtlle moteur droite (-1..1)
        """
        #print('[Robot - Commande moteur] - : Droite = ' + str(gauche) + " + Gauche = " + str(droite))
        self.kit.motor1.throttle = -droite
        self.kit.motor2.throttle = gauche



    def vector_to_differential(self, joy_x, joy_y):
        # CONFIG
        # - fPivYLimit : The threshold at which the pivot action starts
        #                This threshold is measured in units on the Y-axis
        #                away from the X-axis (Y=0). A greater value will assign
        #                more of the joystick's range to pivot actions.
        #                Allowable range: (0..+100)
        
        dead_zone = 10   # Put joy_x and joy_y to 0 if within the dead zone

        
        # deadzone area
        if abs(joy_x) < dead_zone and abs(joy_y) < dead_zone:
            joy_x = 0
            joy_y = 0

        # calculate vector
        angle  = math.atan2(joy_x, joy_y) * 180 / math.pi
        #print('[Robot - differential] - angle vecteur : ' + str(angle))

        # calculate premix drive  due to Joystick Y input
        if abs(joy_y) >= abs(joy_x) and joy_y != 0:
            if joy_x >= 0:
                premix_l = joy_y 
                premix_r = joy_y - joy_x * joy_y / abs(joy_y)
            elif joy_x < 0:
                premix_r = joy_y 
                premix_l = joy_y + joy_x * joy_y / abs(joy_y)
        elif abs(joy_y) < abs(joy_x) and joy_x != 0:
            if joy_x >= 0:
                premix_l = joy_y 
                premix_r = joy_y - joy_x * abs(joy_y / joy_x)
            elif joy_x < 0:
                premix_r = joy_y 
                premix_l = joy_y + joy_x * abs(joy_y / joy_x)
        else:
            premix_r = 0 
            premix_l = 0


        """if joy_y > 0 and joy_x !=0 :
            if joy_x > 0:
                premix_l = joy_y 
                premix_r = joy_y - joy_x * abs(joy_y / joy_x)
            elif joy_x < 0:
                premix_r = joy_y 
                premix_l = joy_y + joy_x * abs(joy_y / joy_x)
        elif joy_y < 0 and joy_x !=0:
            if joy_x > 0:
                premix_l = joy_y 
                premix_r = joy_y + joy_x * abs(joy_y / joy_x)
            elif joy_x < 0:
                premix_r = joy_y 
                premix_l = joy_y - joy_x * abs(joy_y / joy_x)
        else:
            premix_r = joy_y
            premix_l = joy_y 
        """
    
        # calculate pivot amount
        #piv_speed = nJoyX
        #fPivScale = 0.0 if abs(nJoyY)>fPivYLimit else 1.0-abs(nJoyY)/fPivYLimit
        

        """
        # Calculate final mix of Drive and Pivot
        nMotMixL = ((1.0-fPivScale)*nMotPremixL + fPivScale*( nPivSpeed))/100 # Motor (left)  mixed output           (-128..+127)
        nMotMixR = ((1.0-fPivScale)*nMotPremixR + fPivScale*(-nPivSpeed))/100 # Motor (right) mixed output           (-128..+127)
        """

        print('Cmd X Y - Mot G D : ' + str(joy_x) + " " + str(joy_y) + " - " + str(premix_l) + " " + str(premix_r))
         
        #if nMotMixR !=0 :
        #print('[Robot - differential] - Commande moteur D G : ' + str(premix_r) + " " + str(premix_l))
            #print('[Robot - differential] - Commande moteur D G : ' + str(MotMixR) + " " + str(MotMixL))

        return (premix_l, premix_r)
        #self.set_ordre_moteur(premix_l/100, premix_r/100)

       

  