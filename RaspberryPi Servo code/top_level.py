from time import sleep
from threading import Thread
from adafruit_servokit import ServoKit
from midi_file_parse import *

# instantiate servo array from hats
kit = ServoKit(channels=16)

# Servos will be labeled as the following:
# G4_strum, C4_strum, E4_strum, A4_strum for strumming servos
# A4_press, A#_Bb4, B4 for pressing servos 

# servo strum map
G4_strum = kit.servo[12]
C4_strum = kit.servo[13]
E4_strum = kit.servo[14]
A4_strum = kit.servo[15]
# servo fret map
Ab4_press = kit.servo[0]
A4_press = kit.servo[1]
Bb4_press = kit.servo[2]
B4_press = kit.servo[3]
Db4_press = kit.servo[4]
D4_press = kit.servo[5]
Eb4_press = kit.servo[6]
E4_press = kit.servo[7]
F4_press = kit.servo[8]
Gb4_press = kit.servo[9]
C5_press = kit.servo[10]
Db5_press = kit.servo[11]

#Adjust the '140's to each individual servo press amount
note_dictionary = {
    67: [G4_strum, None, None], # G4
    68: [G4_strum, Ab4_press, 130], # G#4
    69: [G4_strum, A4_press, 130], # A4
    70: [G4_strum, Bb4_press, 110], # A#4
    71: [G4_strum, B4_press, 120], # B4
    60: [C4_strum, None, None], # C4
    61: [C4_strum, Db4_press, 85], # C#4
    62: [C4_strum, D4_press, 80], # D4
    63: [C4_strum, Eb4_press, 90], # D#4
    64: [C4_strum, E4_press, 130], # E4
    65: [E4_strum, F4_press, 150], # F4
    66: [E4_strum, Gb4_press, 120], # F#4
    72: [A4_strum, C5_press, 130], # C5
    73: [A4_strum, Db5_press, 140], # C#5
}

press_list = [Ab4_press, A4_press, Bb4_press, B4_press, Db4_press, D4_press, Eb4_press, E4_press, F4_press, Gb4_press, C5_press, Db5_press]

# 500000 microsecs per beat = 120 BPM
# 600000 microsecs per beat = 100 BPM
# chord_dictionary = {
#     "GMaj": [None, D4_Cstring, G4_Estring, B4_Astring],
#     "AbMaj": [], 
#     "AMaj": [],
#     "BbMaj": [],
#     "BMaj": [],
#     "CMaj": [],
#     "DbMaj": [], 
#     "DMaj": [],
#     "EbMaj": [], 
#     "EMaj": [],
#     "FMaj": [],
#     "GbMaj": []
# 
# }


def strum(servo_num):
    angle0  = 0
    angle1  = 40
    current_angle = servo_num.angle
    if(abs(current_angle - angle0) > abs(current_angle - angle1)):
        servo_num.angle = angle0
    else:
        servo_num.angle = angle1

def press(servo_num, press_amount):
    if(servo_num == None or press_amount == None):
        return
    angle = press_amount
    servo_num.angle = angle

def unpress(servo_num):
    if(servo_num == None):
        return
    angle = 180
    servo_num.angle = angle

def note(servo_strum, servo_press, press_amount, duration):
    press(servo_press, press_amount)
    sleep(0.1)
    strum(servo_strum)
    sleep(duration)
    unpress(servo_press)

def initialize():
    G4_strum.angle = 0
    A4_strum.angle = 0
    C4_strum.angle = 0
    E4_strum.angle = 0
    for item in press_list:
        unpress(item)
    sleep(1)
    

"""def GMaj(duration):
  note(G_strum, None, duration)
  note(C_strum, D4_C_string, duration)
  note(E_strum, G4_E_string, duration)
  note(A_strum, B4_A_string, duration)"""


""" This code works to test a simple song
note(G4_strum, None, 1)
note(G4_strum, F4_press, 1)
note(G4_strum, Eb4_press, 2)"""

initialize()
# Play song from file
#while True:
for pair in notes_in_song:
    note(note_dictionary.get(pair[0])[0],
         note_dictionary.get(pair[0])[1],
         note_dictionary.get(pair[0])[2],
         pair[1])
# initialize()


# Play C chord
# press(C5_press, 130)
# sleep(0.1)
# strum(G4_strum)
# strum(C4_strum)
# strum(E4_strum)
# strum(A4_strum)

# press(note_dictionary.get(62)[1], note_dictionary.get(62)[2])
# press(note_dictionary.get(62)[1], note_dictionary.get(62)[2])
# press(note_dictionary.get(62)[1], note_dictionary.get(62)[2])


"""note(A4_strum, C5_press, 130, 1)
note(G4_strum, None, None, 1)
note(C4_strum, None, None, 1)
note(E4_strum, None, None, 1)"""

# initialize()

# note(A4_strum, Db5_press, 140, 5)

#test_unpress(Ab4_press)
#test_press(Ab4_press)

#strum(E4_strum)