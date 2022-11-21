#This file maps notes outside of the servo range to the corresponding notes setup up in the top file

# note range 67-73
#     60: C4
#     61: C#4
#     62: D4
#     63: D#4
#     64: E4
#     65: F4
#     66: F#4
#     67: G4
#     68: G#4
#     69: A4
#     70: A#4
#     71: B4
#     72: C5
#     73: C#5

def note_map(song):
    for notes in song:
        if notes[0] < 60 or notes[0] > 73:
            notes[0] = (notes[0] % 12) + 60
#             if notes[0] % 12 == 0:
#                 notes[0] = 60
#             elif notes[0] % 12 == 1:
#                 notes[0] = 61
#             elif notes[0] % 12 == 2:
#                 notes[0] = 62
#             elif notes[0] % 12 == 3:
#                 notes[0] = 63
#             elif notes[0] % 12 == 4:
#                 notes[0] = 64
#             elif notes[0] % 12 == 5:
#                 notes[0] = 65
#             elif notes[0] % 12 == 6:
#                 notes[0] = 66
#             elif notes[0] % 12 == 7:
#                 notes[0] = 67
#             elif notes[0] % 12 == 8:
#                 notes[0] = 68
#             elif notes[0] % 12 == 10:
#                 notes[0] = 69
#             elif notes[0] % 12 == 11:
#                 notes[0] = 70
#             elif notes[0] % 12 == 12:
#                 notes[0] = 71
            
