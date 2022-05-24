#!/usr/bin/env python3
import midi_abstraction

for k in midi_abstraction.list_keys():
	song_key = midi_abstraction.Key(k)

	# attributes
	print(f'key: {song_key.name}')
	print(f'mode: {song_key.mode}')
	print(f'chords: {song_key.chords}')
	print(f'notes: {song_key.notes}')
	try:
		print(f'relative key: {song_key.relative_key}')
	except Exception as e:
		print(e)
  
	# list functions
	print(f'list_notes(): {song_key.list_notes()}')
	print(f'list_chords(): {song_key.list_chords()}')
	print(f'list_relative_chords(): {song_key.list_relative_chords()}')
	print(f'list_chords_in_relative_key(): {song_key.list_chords_in_relative_key()}')
	print(f'list_notes_in_octave(5): {song_key.list_notes_in_octave(5)}')
	print(f'list_notes_in_pentatonic_major(): {song_key.list_notes_in_pentatonic_major()}')
	print(f'list_notes_in_pentatonic_minor(): {song_key.list_notes_in_pentatonic_minor()}')

	# dict functions
	print(f'chords_in_octave(5): {song_key.chords_in_octave(5)}')
	print(f'notes_in_pentatonic_minor(): {song_key.notes_in_pentatonic_minor()}')
	print(f'notes_in_pentatonic_major(): {song_key.notes_in_pentatonic_major()}')


# root functions not associated with Key class.
print(f'midi_abstraction.list_modes(): {midi_abstraction.list_modes()}')
print(f'midi_abstraction.universe(): {midi_abstraction.universe()}')
for i in midi_abstraction.list_notes():
	print(f'midi_abstraction.notes({i}): {midi_abstraction.notes(i)}')

# midi_abstraction.list_keys is handled above

print(f'midi_abstraction.drums_dict(): {midi_abstraction.drums_dict()}')

for i in midi_abstraction.drums_dict().keys():
	print(f'midi_abstraction.drums({i}): {midi_abstraction.drums(i)}')

for i in midi_abstraction.drums_dict().values():
	print(f'midi_abstraction.drums({i}): {midi_abstraction.drums(i)}')


