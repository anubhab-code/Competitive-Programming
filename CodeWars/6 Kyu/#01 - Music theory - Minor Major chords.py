notes = ['C', '', 'C#', 'Db', 'D', '', 'D#', 'Eb', 'E', '', 'F', '',
          'F#', 'Gb', 'G', '', 'G#', 'Ab', 'A', '', 'A#', 'Bb', 'B']

def minor_or_major(chord):
    try:
        chordpos = [notes.index(c) // 2 for c in chord.split()]
    except:
        return "Not a chord"
    if len(chordpos) == 3:
        interval1 = (chordpos[1] - chordpos[0]) % 12
        interval2 = (chordpos[2] - chordpos[1]) % 12
        if interval1 == 3 and interval2 == 4:
            return "Minor"
        if interval1 == 4 and interval2 == 3:
            return "Major"
    return "Not a chord"