import RPi.GPIO as GPIO


"""
pour pololu #4868
pleine vitesse = 43 x 171.79 tr /mn de l'axe
soit 7386.97 /60 / 10 = 12.3116 sample du moteur
soit 12.3116 x 24  = 295 ticks / sample
"""

class Encoder(object): 
    """
    Encoder class allows to work with rotary encoder
    which connected via two pin A.
    """
    def __init__(self, A):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(A, GPIO.IN)
        self.A = A
        self.pos = 0
        GPIO.add_event_detect(A, GPIO.BOTH, callback=self.__update)

    """
    update() calling every time when value on A pins changes.
    It updates the current position based on previous and current states
    of the rotary encoder.
    """
    def __update(self, channel):
        self.pos += 1

    """
    reset()
    simply reset position
    """
    def reset(self):
        self.pos = 0

    """
    read() simply returns the current position of the rotary encoder.
    """
    def read(self):
        return self.pos  

 