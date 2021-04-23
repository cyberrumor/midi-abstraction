# midi_abstraction

Abstract midi pitches into keys, chords, modes, scales, and notes.

This, combined with a midi file creation package like 'mido', and maybe a little help from builtin 'random', is all you need to procedurally generate music.


# Installation
```pip install midi_abstraction```

# Usage

```
#!/usr/bin/env python3
import midi_abstraction

# create a key object. Note + either major or minor or modename
k = midi_abstraction.Key('d_dorian')

# available list methods
k.list_notes()
k.list_chords()
k.list_notes_in_octave(3)
k.list_notes_in_pentatonic_minor()
k.list_notes_in_pentatonic_major()

# available dict methods
k.chords_in_octave(3)
k.notes_in_pentatonic_minor()
k.notes_in_pentatonic_major()


# attributes
k.name
k.seniority
k.mode
k.chords
k.notes

### functions not tied to a class ###

# get the midi pitches of a specific note
midi_abstraction.notes('a')

# get midi pitch of a specific note in specific cotave
midi_abstraction.notes('cs')[4]

# get a list of all available notes
midi_abstraction.list_notes()

# get a list of major and minor keys (doesn't list modal keys)
midi_abstraction.list_keys()

# get a list of mode names
midi_abstraction.list_modes()

# if you need to iterate through note names and don't want to hit an out of range index, use universe:
midi_abstraction.universe()

# get the midi pitches of notes in a specific chord:
midi_abstraction.chords('c_major')

# you can also invent your own chords like this if you want to get weird.
midi_abstraction.chords('cs_e_ab')


#### examples of how to use ######
# get a random modal key and create an instance of it.
import random
n = random.choice(midi_abstraction.list_notes())
m = random.choice(midi_abstraction.list_keys())
k = midi_abstraction.Key(n + '_' + m)

# get some chords
first = k.list_chords()[0]
second = random.choice(k.list_chords())
third = random.choice(k.list_chords())

# you need mido to write midi files
import mido

# you can use a loop on [first, second, third] to push the pitches into mido tracks.
# See https://github.com/cyberrumor/keygen/blob/main/keygen.py for an example implementation. 
# Good luck!

```
