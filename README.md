# midi_abstraction

Abstract midi pitches into keys, chords, and notes.

Now supports diatonic and pentatonic chords!

This does not yet support modes [Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian], but it will soon.

# Installation
```pip3 install midi_abstraction```

# Usage
```
#!/usr/bin/env python3
import random
import json
import midi_abstraction

if __name__ == '__main__':

	# get a list of all available keys.
	all_keys = midi_abstraction.list_key_names()
	print('list of all keys:')
	for option in all_keys:
		print(option)
	print()

	# get a key at random
	our_key = random.choice(all_keys)
	print(f'our_key: {our_key}')
	print()

	# Initialize the musical key object
	Song_key = midi_abstraction.Key(our_key)

	# Print all notes found in chords in the key, in the lowest octave.
	print(f'Song_key.notes_in_octave(0): {json.dumps(Song_key.notes_in_octave(0), indent = 4, sort_keys = True)}')
	print()

	# Print all chords in the key, all modes, in the lowest octave.
	print(f'Song_key.chords_in_octave(0): {json.dumps(Song_key.chords_in_octave(0), indent = 4, sort_keys = True)}')
	print()

	# Print key chords in all modes and octaves.
	# print(f'Song_key.chords: {json.dumps(Song_key.chords, indent = 4, sort_keys = True)}')
	# or
	print(f'Song_key.chords_in_key(): {json.dumps(Song_key.chords_in_key(), indent = 4, sort_keys = True)}')


	# Print all notes in key, all modes, all octaves
	print(f'Song_key.notes_in_key(): {Song_key.notes_in_key()}')

	# Print pentatonic chords, all octaves.
	print(f'Song_key.pentatonic_chords(): {Song_key.pentatonic_chords()}')

	# Print pentatonic chords in 5th octave.
	print(f'Song_key.pentatonic_chords_in_octave(5): {Song_key.pentatonic_chords_in_octave(5)}')

```
