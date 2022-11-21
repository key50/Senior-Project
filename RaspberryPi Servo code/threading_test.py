from time import sleep
from threading import Thread
from adafruit_servokit import ServoKit

LOS = ServoKit(channels=16)

tempo1 = 0.25
tempo2 = 0.5

def move1(tempo):
    angle0 = 0
    angle1 = 30
    while(True):
        LOS.servo[0].angle = angle0
        sleep(tempo)
        LOS.servo[0].angle = angle1
        sleep(tempo)
        
def move2(tempo):
    angle0 = 0
    angle1 = 30
    while(True):
        LOS.servo[1].angle = angle0
        sleep(tempo)
        LOS.servo[1].angle = angle1
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