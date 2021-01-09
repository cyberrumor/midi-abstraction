# midi_abstraction

Abstract midi pitches into keys, chords, modes and notes.

This, combined with a midi file creation package like 'mido', and maybe a little help from builtin 'random', is all you need to procedurally generate music.


# Installation
```pip install midi_abstraction```

# Usage

```
#!/usr/bin/env python3
import midi_abstraction

# get a list of keys
available_keys = midi_abstraction.list_key_names()

# get a list of available notes
available_notes = midi_abstraction.list_note_names()

# get a list of available modes
available_modes = midi_abstraction.list_mode_names()

# create a musical key object
songkey = midi_abstraction.Key('a_major')

# list chords in the key
songkey.list_chord_names()

# list note names in mode
songkey.list_note_names_in_mode('mixolydian')

# list midi note pitches in specific octave
songkey.list_notes_in_octave(4)

# access a dict of chords in songkey here.
chords = songkey.chords
# you can also access modes like this.
ionian = songkey.ionian


# iterate through the chords to get midi pitches.
for key, value in songkey.chords.items():
	print(f'{key}: {value})

# print chord names and midi pitches of the notes in each chord, specifying octave.
print(songkey.chords_in_octave(4))

```
