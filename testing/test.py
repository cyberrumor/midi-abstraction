#!/usr/bin/env python3
import midi_abstraction

for k in midi_abstraction.list_keys():
	song_key = midi_abstraction.Key(k)

	print(f'key: {k}')
	for mode in midi_abstraction.list_modes():
		print(f'{mode}: {song_key.list_notes_in_mode(mode)}')


	print(f'pentatonic minor: {song_key.notes_in_pentatonic_minor()}')
	print(f'pentatonic major: {song_key.notes_in_pentatonic_major()}')

	print(f'list pent minor: {song_key.list_notes_in_pentatonic_minor()}')
	print(f'list pent major: {song_key.list_notes_in_pentatonic_major()}')

	print(f'numerals: {song_key.numerals}')

print(f'song_key.universal_notes: {song_key.universal_notes}')


