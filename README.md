# midi_abstraction
Abstract midi pitches into keys, chords, and notes.

# Classes
Provides the following classes:

Notes - this owns note names such as Cs and Ab.

Key - this owns all chords from the declared key during initialization.
	- initialize with Key('c_major')
	- before init, get a list of available keys with Key.list_key_names()
	- each initialized key will hold objects like chords, notes, chords_in_octave, notes_in_octave.
	- for those methods, pass octave as an argument, range(0, 11).

