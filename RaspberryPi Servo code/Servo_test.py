from gpiozero import AngularServo
from time import sleep


s = AngularServo(11, min_pulse_width = 0.0006, max_pulse_width = 0.0023)

while True:
    s.min()
    sleep(1)
    s.mid()
    sleep(1)
    s.max()
    sleep(1)
    
    
