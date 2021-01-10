# midi_abstraction

Abstract midi pitches into keys, chords, modes, scales, and notes.

This, combined with a midi file creation package like 'mido', and maybe a little help from builtin 'random', is all you need to procedurally generate music.


# Installation
```pip install midi_abstraction```

# Usage

```
#!/usr/bin/env python3
import midi_abstraction

# get a list of keys
available_keys = midi_abstraction.list_keys()

# get a list of available notes
available_notes = midi_abstraction.list_notes()

# get a list of available modes
available_modes = midi_abstraction.list_modes()

# create a musical key object
songkey = midi_abstraction.Key('a_major')

# list chords in the key
songkey.list_chords()

# list note names in mode
songkey.list_notes_in_mode('mixolydian')

# list midi note pitches in specific octave
songkey.list_notes_in_octave(4)

# access a dict of chords in songkey here.
chords = songkey.chords

# access pentatonic major and minor scales
pentatonic_major = songkey.list_notes_in_pentatonic_major()
pentatonic_minor = songkey.list_notes_in_pentatonic_minor()

# iterate through the chords to get midi pitches.
for key, value in songkey.chords.items():
	print(f'{key}: {value})

# print chord names and midi pitches of the notes in each chord, specifying octave.
print(songkey.chords_in_octave(4))

# turn any named note into a midi pitch
notes = Notes()
c_sharp_pitch = notes.all['cs']

# get any chord from any key, or pitches of any note outside of the key
songkey.universal_chords
songkey.universal_notes

```
