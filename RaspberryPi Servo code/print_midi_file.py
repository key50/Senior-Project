# This is for parsing the MIDI file to see what information it has

from mido import MidiFile
from mido import second2tick

filename = '/home/pi/Desktop/RaspberryPi Servo code/midis/hot_cross_bunsTPT.mid'
    
midi_file = MidiFile(filename)
ticks_per_beat = midi_file.ticks_per_beat 
tempo = 600000

for msg in midi_file:
    if(msg.type == 'note_on'):
        print(f'Note on: {msg.note} Duration: {second2tick(msg.time, ticks_per_beat, tempo)}')
    if(msg.type == 'note_off'):
        print(f'Note off: {msg.note} Duration {second2tick(msg.time, ticks_per_beat, tempo)}')
