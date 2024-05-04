# midi_abstraction

Abstract midi pitches into keys, chords, modes, scales, and notes.

# Installation
```
# From pip
pip install midi_abstraction

# From source
pip3 install --user --break-system-packages .
```
- requires python 3.10 or newer

# Usage
```
#!/usr/bin/env python3
import midi_abstraction as mab

# Get a midi note from a letter
octave = 4
middle_c = mab.NOTES["c"][octave]

# Get a letter note from a midi pitch
some_note = None
for k, v in mab.NOTES.items():
    if 48 in v:
        some_note = k
        break

# Get a pitch for a drum
side_stick = mab.Drum.SIDE_STICK.value

# Get a drum from a pitch
some_drum = mab.Drum(35)

# List all drums
list(mab.Drum)

# List all chord names
list(mab.Chord)

# Get the note names that a chord is made of
c_major_notes = mab.CHORDS['c_major']


# Get the notes and chords from any mode/key.
# These are a list of sets due to enharmonic equivalence.
c_major_chords = mab.MAJOR.chords('c')
eb_phrygian_notes = mab.PHRYGIAN.notes('eb')

# Get chords from scale degrees
third_degree_chord = next(iter(mab.MAJOR.chords('c')[2]))

# Get the notes for a chord in a particular octave
octave = 4
middle_c_major_notes = []
for note in mab.CHORDS['c_major']:
    middle_c_major_notes.append(mab.NOTES[note][octave])

```

