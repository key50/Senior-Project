import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
angle = 30
tempo = 1.0

def move1(tempo):
    start = time.monotonic()
    kit.servo[0].angle = 0
    while(True):
        now = time.monotonic()
        if(tempo < now - start):
            kit.servo[0].angle = 180
            break;
    start2 = time.monotonic();
    while(True):
        now = time.monotonic()
        if(tempo < now - start2):
            kit.servo[0].angle = 0
            break;
def move2(tempo):
    start = time.monotonic()
    kit.servo[1].angle = 0
    while(True):
        now = time.monotonic()
        if(tempo < now - start):
            kit.servo[1].angle = 180
            break;
    start2 = time.monotonic();
    while(True):
        now = time.monotonic()
        if(tempo < now - start2):
            kit.servo[1].angle = 0
            break;
        
def move3(tempo):
    kit.servo[2].angle = 0
    sleep(tempo)
    kit.servo[2].angle = 180
    sleep(tempo)
    
def move4(tempo):
    kit.servo[3].angle = 0
    sleep(tempo)
    kit.servo[3].angle = 180
    sleep(tempo)

while True:
    move1(tempo)
    move2(tempo)
    #move3(tempo)
    #move4(tempo)
