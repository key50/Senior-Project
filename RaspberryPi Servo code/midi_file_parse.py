# This is for creating a list with (note_value, duration)

from mido import MidiFile
from range_mapping import *


#filename = '/home/pi/Desktop/RaspberryPi Servo code/midis/hot_cross_bunsTPT.mid'
filename = '/home/pi/Desktop/RaspberryPi Servo code/midis/happy_birthday.mid'

    
midi_file = MidiFile(filename)
notes_in_song = []

for msg in midi_file:
    if(msg.type == 'note_off'):
        notes_in_song.append([msg.note, msg.time])
    #print(f'Note off: {msg.note} Duration {second2tick(msg.time, ticks_per_beat, tempo)}')

print(notes_in_song)

note_map(notes_in_song)
print('\n')

print(notes_in_song)