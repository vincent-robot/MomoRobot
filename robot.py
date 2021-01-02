import time
import math
from datetime import datetime
from adafruit_motorkit import MotorKit

def lin2log(x):
    """ Return logatitmic value of the given x provided as an input
    
    Keyword arguments:
    x : input to be transformed [x0..x1]
    """
    x0 = 1
    x1 = 100

    if x < x0 or x > x1:
        raise ValueError ("Input must be beetween %s and %s" %(x0, x1))

    scale = (math.log(x1)-math.log(x0)) / (x1 - x0)
    return round(math.exp((x-x0) * scale))


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
        """ Transform Joystick coordinate to differential throtlle for L and R motor

        Keyword arguments:
        joy_x : Joystick x position (-100..100)
        joy_y : Joystick y position (-100..100)
        """

        dead_zone = 10   # Put joy_x and joy_y to 0 if within the dead zone
        
        joy_x = min(joy_x, 100)
        joy_y = min(joy_y, 100)

        
        # deadzone area
        if abs(joy_x) < dead_zone: 
            joy_x = 0
        if abs(joy_y) < dead_zone:
            joy_y = 0
        #otherwise chanage x axis on log scale
        if joy_x > 0:
            joy_x = (lin2log(joy_x) * joy_x) / 2
        elif joy_x < 0:
            joy_x = (lin2log(abs(joy_x)) * joy_x)/ 2
        
        #angle  = math.atan2(joy_x, joy_y) * 180 / math.pi
        #print('[Robot - differential] - angle vecteur : ' + str(angle))

        # calculate drive forward / reward (both motor in the same direction)
        if abs(joy_y) >= abs(joy_x) and joy_y != 0:
            if joy_x >= 0:
                premix_l = joy_y 
                premix_r = joy_y - joy_x * joy_y / abs(joy_y)
            elif joy_x < 0:
                premix_r = joy_y 
                premix_l = joy_y + joy_x * joy_y / abs(joy_y)
        # calculate drive for rotation (revert motor)
        elif abs(joy_y) < abs(joy_x) and joy_x != 0:        
            if joy_x >= 0:
                premix_l = joy_x /2
                premix_r = - joy_x /2
            elif joy_x < 0:
                premix_r = -joy_x / 2
                premix_l = joy_x / 2
        else:
            premix_r = 0 
            premix_l = 0

        print('Cmd X Y - Mot G D : ' + str(joy_x) + " " + str(joy_y) + " - " + str(premix_l) + " " + str(premix_r))

        return (premix_l, premix_r)
        #self.set_ordre_moteur(premix_l/100, premix_r/100)

       

  