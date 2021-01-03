#!/usr/bin/env python3
import midi_abstraction

a_major = midi_abstraction.Key('a_major')
a_minor = midi_abstraction.Key('a_minor')
b_major = midi_abstraction.Key('b_major')
b_minor = midi_abstraction.Key('b_minor')
c_major = midi_abstraction.Key('c_major')
c_minor = midi_abstraction.Key('c_minor')
d_major = midi_abstraction.Key('d_major')
d_minor = midi_abstraction.Key('d_minor')
e_major = midi_abstraction.Key('e_major')
e_minor = midi_abstraction.Key('e_minor')
f_major = midi_abstraction.Key('f_major')
f_minor = midi_abstraction.Key('f_minor')
g_major = midi_abstraction.Key('g_major')
g_minor = midi_abstraction.Key('g_minor')

all_keys = [
	a_major,
	a_minor,
	b_major,
	b_minor,
	c_major,
	c_minor,
	d_major,
	d_minor,
	e_major,
	e_minor,
	f_major,
	f_minor,
	g_major,
	g_minor
]

for i in all_keys:
	print()
	print(f'{i.name}.name: {i.name}')
	print()
	print(f'{i.name}.chords_in_octave(3): {i.chords_in_octave(3)}')
	print()
	print(f'{i.name}.diatonic_chords(): {i.diatonic_chords()}')
	print()
	print(f'{i.name}.diatonic_chords_in_octave(3): {i.diatonic_chords_in_octave(3)}')
	print()
	print(f'{i.name}.pentatonic_chords(): {i.pentatonic_chords()}')
	print()
	print(f'{i.name}.pentatonic_chords_in_octave(3): {i.pentatonic_chords_in_octave(3)}')
	print()
	print(f'{i.name}.notes_in_octave(3): {i.notes_in_octave(3)}')
	print()
	print(f'{i.name}.notes_in_key(): {i.notes_in_key()}')
	print()
	print(f'{i.name}.chords_in_key(): {i.chords_in_key()}')
	print()








