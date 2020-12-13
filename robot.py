import time
from adafruit_motorkit import MotorKit
from datetime import datetime


class Robot:
    def __init__(self):
        self.kit = MotorKit()

    def set_ordre_moteur(self, droite, gauche):
        self.kit.motor1.throttle = -droite
        self.kit.motor2.throttle = gauche