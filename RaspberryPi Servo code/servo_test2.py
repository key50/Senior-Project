from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo
from time import sleep
from threading import Thread

fact = PiGPIOFactory() 

servo1 = AngularServo(18,min_pulse_width = 0.0006, max_pulse_width = 0.0023, pin_factory = fact)
servo2 = AngularServo(17,min_pulse_width = 0.0006, max_pulse_width = 0.0023, pin_factory = fact)

tempo1 = 0.25
tempo2 = 0.5

def move1(tempo):
    angle = 30
    while(True):
        servo1.angle = -angle
        sleep(tempo)
        servo1.angle = angle
        sleep(tempo)
        
def move2(tempo):
    angle = 30
    while(True):
        servo2.angle = -angle
        sleep(tempo)
        servo2.angle = angle
        sleep(tempo)
    
threading = []

x = Thread(target=move1, args=(tempo1,))
threading.append(x)
y = Thread(target=move2, args=(tempo2,))
threading.append(y)



""" Hello, I worked on Multithreading while you were gone. This will allow us to play each
    servo at its own tempo. Run it to see that 1 moves at 0.5 and 2 moves at 0.25.
    Pretty nice.
"""

#while (True):
x.start()
y.start()
    