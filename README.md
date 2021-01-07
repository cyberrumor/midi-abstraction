# midi_abstraction

Abstract midi pitches into keys, chords, modes and notes.

This, combined with a midi file creation package like 'mido', and maybe a little help from builtin 'random', is all you need to procedurally generate music.


# Installation
```pip install midi_abstraction```

# Usage

```
#!/usr/bin/env python3
import midi_abstraction


# list all keys
all_keys = midi_abstraction.list_key_names()

# list all modes
all_modes = midi_abstraction.list_mode_names()

# list all notes
all_notes = midi_abstraction.list_note_names()

# Methods that return lists start with 'lists'.
# others that return lists end with 'names'.
# everything else returns a dictionary.

# let's pick an octave to write music in.
octave = 3

our_song_key = midi_abstraction.Key('a_major')
print(f'aware of name: {our_song_key.name}')
print()

for name_of_mode in our_song_key.list_mode_names():
	print()
	print(f'dict of mode is here for easy access: our_song_key.{name_of_mode}')
	print()
	print(f'list chords in specific mode: our_song_key.list_chords_in_mode("{name_of_mode}")')
	print()
	print('we also have access to all chords/notes in specific mode and specific octave:')
	print()
	print(f'our_song_key.chords_in_modal_octave("{name_of_mode}", {octave}): {our_song_key.chords_in_modal_octave(name_of_mode, octave)}')
	print()

print(f'list of chords and their notes in specific octave: {our_song_key.chords_in_octave(octave)}')
print()
print(f'list of chord names: {our_song_key.list_chord_names()}')
print()
print(f'seniority: {our_song_key.seniority}')
print()

print('If we want a list of midi pitches for a named note instead of a chord or key, we can get it like this:')
print()
print('note = midi_abstraction.Notes()')
note = midi_abstraction.Notes()
print()
print(f'note.As: {note.As} \n\n note.As[{octave}]: {note.As[octave]}')
print()
```






