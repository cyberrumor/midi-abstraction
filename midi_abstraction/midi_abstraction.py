#!/usr/bin/env python3
class Notes:
	def __init__(self):
		self.As = [i * 12 + 10 for i in range(0, 10)]
		self.A = [i * 12 + 9 for i in range(0, 10)]
		self.B = [i * 12 + 11 for i in range(0, 10)]
		self.Cs = [i * 12 + 1 for i in range(0, 11)]
		self.C = [i * 12 for i in range(0, 11)]
		self.Ds = [i * 12 + 3 for i in range(0, 11)]
		self.D = [i * 12 + 2 for i in range(0, 11)]
		self.E = [i * 12 + 4 for i in range(0, 11)]
		self.Es = [i * 12 + 5 for i in range(0, 11)]
		self.Fs = [i * 12 + 6 for i in range(0, 11)]
		self.F = [i * 12 + 5 for i in range(0, 11)]
		self.Gs = [i * 12 + 8 for i in range(0, 10)]
		self.G = [i * 12 + 7 for i in range(0, 11)]
		self.Ab = [i * 12 + 8 for i in range(0, 10)]
		self.Bb = [i * 12 + 10 for i in range(0, 10)]
		self.Db = [i * 12 + 1 for i in range(0, 11)]
		self.Eb = [i * 12 + 3 for i in range(0, 11)]
		self.Gb = [i * 12 + 6 for i in range(0, 11)]

	def list_notes(self):
		return list_note_names()

class Key:
	def __init__(self, name):
		self.name = name
		notes = Notes()
		chords = {
			'a_minor': [notes.A, notes.C, notes.E],
			'a_minor_seventh': [notes.A, notes.C, notes.E, notes.G],
			'as_dim': [notes.As, notes.Cs, notes.E],
			'as_minor_seventh_flat_five': [notes.As, notes.Cs, notes.E, notes.Gs],
			'as_major': [notes.As, notes.D, notes.F],
			'as_minor': [notes.As, notes.Cs, notes.Es],
			'a_major': [notes.A, notes.Cs, notes.E],
			'a_dim': [notes.A, notes.C, notes.Eb],
			'a_major_seventh': [notes.A, notes.Cs, notes.E, notes.Gs],
			'a_dom_seventh': [notes.A, notes.Cs, notes.E, notes.G],
			'ab_major': [notes.Ab, notes.C, notes.Eb],
			'ab_major_seventh': [notes.Ab, notes.C, notes.Eb, notes.G],
			'bb_major_seventh': [notes.Bb, notes.D, notes.F, notes.A],
			'bb_major': [notes.Bb, notes.D, notes.F],
			'bb_dom_seventh': [notes.Bb, notes.D, notes.F, notes.Ab],
			'b_dim': [notes.B, notes.D, notes.F],
			'b_minor_seventh_flat_five': [notes.B, notes.D, notes.F, notes.A],
			'b_major': [notes.B, notes.Ds, notes.Fs],
			'b_major_seventh': [notes.B, notes.Ds, notes.Fs, notes.As],
			'b_minor': [notes.B, notes.D, notes.Fs],
			'b_minor_seventh': [notes.B, notes.D, notes.Fs, notes.A],
			'cs_dim': [notes.Cs, notes.E, notes.G],
			'cs_major': [notes.Cs, notes.F, notes.G],
			'cs_minor_seventh_flat_five': [notes.Cs, notes.E, notes.G, notes.B],
			'cs_minor': [notes.Cs, notes.E, notes.Gs],
			'cs_minor_seventh': [notes.Cs, notes.E, notes.Gs, notes.B],
			'c_major': [notes.C, notes.E, notes.G],
			'c_dim': [notes.C, notes.Eb, notes.Gb],
			'c_major_seventh': [notes.C, notes.E, notes.G, notes.B],
			'c_minor': [notes.C, notes.Eb, notes.G],
			'c_minor_seventh': [notes.C, notes.Eb, notes.G, notes.Bb],
			'c_dom_seventh': [notes.C, notes.E, notes.G, notes.Bb],
			'ds_major': [notes.Ds, notes.G, notes.As],
			'ds_dim': [notes.Ds, notes.Fs, notes.A],
			'ds_minor': [notes.Ds, notes.Fs, notes.As],
			'ds_minor_seventh': [notes.Ds, notes.Fs, notes.As, notes.Cs],
			'd_major': [notes.D, notes.Fs, notes.A],
			'd_major_seventh': [notes.D, notes.Fs, notes.A, notes.Cs],
			'd_minor': [notes.D, notes.F, notes.A],
			'd_minor_seventh': [notes.D, notes.F, notes.A, notes.C],
			'd_dim': [notes.D, notes.F, notes.Ab],
			'd_minor_seventh_flat_five': [notes.D, notes.F, notes.Ab, notes.C],
			'e_major': [notes.E, notes.Gs, notes.B],
			'e_major_seventh': [notes.E, notes.Gs, notes.B, notes.Ds],
			'e_dom_seventh': [notes.E, notes.Gs, notes.B, notes.D],
			'e_minor': [notes.E, notes.G, notes.B],
			'e_minor_seventh': [notes.E, notes.G, notes.B, notes.D],
			'eb_major': [notes.Eb, notes.G, notes.Bb],
			'eb_major_seventh': [notes.Eb, notes.G, notes.Bb, notes.D],
			'e_dim': [notes.E, notes.G, notes.Bb],
			'e_minor_seventh_flat_five': [notes.E, notes.G, notes.Bb, notes.D],
			'fs_minor': [notes.Fs, notes.A, notes.Cs],
			'fs_minor_seventh': [notes.Fs, notes.A, notes.Cs, notes.E],
			'f_major': [notes.F, notes.A, notes.C],
			'f_dim': [notes.F, notes.Ab, notes.B],
			'f_major_seventh': [notes.F, notes.A, notes.C, notes.E],
			'fs_major': [notes.Fs, notes.As, notes.Cs],
			'fs_dim': [notes.Fs, notes.A, notes.C],
			'fs_dom_seventh': [notes.Fs, notes.As, notes.Cs, notes.E],
			'f_minor': [notes.F, notes.Ab, notes.C],
			'gs_major': [notes.Gs, notes.C, notes.Ds],
			'gs_minor': [notes.Gs, notes.B, notes.Ds],
			'gs_minor_seventh': [notes.Gs, notes.B, notes.Ds, notes.Fs],
			'gs_dim': [notes.Gs, notes.B, notes.D],
			'gs_minor_seventh_flat_five': [notes.Gs, notes.B, notes.D, notes.Fs],
			'g_major': [notes.G, notes.B, notes.D],
			'g_dim': [notes.G, notes.Bb, notes.Db],
			'g_dom_seventh': [notes.G, notes.B, notes.D, notes.F],
			'g_major_seventh': [notes.G, notes.B, notes.D, notes.Fs],
			'g_minor': [notes.G, notes.Bb, notes.D],
			'g_minor_seventh': [notes.G, notes.Bb, notes.D, notes.F]
		}

		universe = ['a', 'as', 'b', 'c', 'cs', 'd', 'ds', 'e', 'f', 'fs', 'g', 'gs'] * 2
		W = 2
		H = 1
		if 'major' in name.lower() and name[0].lower() in universe:
			if name[1].lower() == 's':
				root = universe.index(''.join(name[0:3]))
			elif name[1] == '_':
				root = universe.index(name[0])
			elif name[1].lower() == 'b':
				check = universe.index(name[0]) - 1
				root = universe.index(check)
			else:
				raise NameError(f'{name} is not a valid musical key.')

			default_mode = [W, W, H, W, W, W, H]
			numerals = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'viid']

		elif 'minor' in name.lower() and name[0] in universe:
			if name[1].lower() == 's':
				root = universe.index(''.join(name[0:3]))
			elif name[1] == '_':
				root = universe.index(name[0])
			elif name[1].lower() == 'b':
				check = universe.index(name[0]) - 1
				root = universe.index(check)
			else:
				raise NameError(f'{name} is not a valid musical key.')

			default_mode = [W, H, W, W, H, W, W]
			numerals = ['i', 'iid', 'III', 'iv', 'v', 'VI', 'VII']
		else:
			raise NameError(f'{name} is not a valid musical key.')

		# get the notes for each mode
		slice = universe[root:]
		ionian = default_mode
		dorian = [default_mode[6]] + default_mode[0:6]
		phrygian = default_mode[5:] + default_mode[0:5]
		lydian = default_mode[4:] + default_mode[0:4]
		mixolydian = default_mode[3:] + default_mode[0:3]
		aeolian = default_mode[2:] + default_mode[0:2]
		locrian = default_mode[1:] + [default_mode[0]]

		rough_modes = {
			'ionian': {'steps': ionian, 'notes': []},
			'dorian': {'steps': dorian, 'notes': []},
			'phrygian': {'steps': phrygian, 'notes': []},
			'lydian': {'steps': lydian, 'notes': []},
			'mixolydian': {'steps': mixolydian, 'notes': []},
			'aeolian': {'steps': aeolian, 'notes': []},
			'locrian': {'steps': locrian, 'notes': []}
		}

		modes = {}
		for key in list(rough_modes.keys()):
			index = 0
			modes[key] = {}
			modes[key]['chords'] = {}
			for step in range(len(rough_modes[key]['steps'])):
				if numerals[step].isupper() and 'd' not in numerals[step]:
					name = slice[index] + '_major'
				elif numerals[step].isupper() and 'd' in numerals[step]:
					name = slice[index] + '_major_dim'
				elif numerals[step].islower() and 'd' not in numerals[step]:
					name = slice[index] + '_minor'
				elif numerals[step].islower() and 'd' in numerals[step]:
					name = slice[index] + '_dim'

				modes[key]['chords'][name] = chords[name]
				index += rough_modes[key]['steps'][step]

		self.raw_modal_database = modes
		self.chords = modes['ionian']['chords']
		self.ionian = modes['ionian']['chords']
		self.dorian = modes['dorian']['chords']
		self.phrygian = modes['phrygian']['chords']
		self.lydian = modes['lydian']['chords']
		self.mixolydian = modes['mixolydian']['chords']
		self.aeolian = modes['aeolian']['chords']
		self.locrian = modes['locrian']['chords']

		if 'major' in self.name:
			self.seniority = 'major'
		else:
			self.seniority = 'minor' 

	# RETURNS LIST
	def list_chord_names_in_mode(self, modename):
		return [i for i in list(self.raw_modal_database[modename]['chords'].keys())]

	def list_chord_names(self):
		return [i for i in list(self.chords.keys())]

	def list_mode_names(self):
		return list_mode_names()

	def list_notes_in_key(self):
		new_list = []
		for key, value in self.chords_in_mode('ionian').items():
			for chord in value:
				for note in chord:
					if note not in new_list:
						new_list.append(note)
		new_list.sort()
		return new_list

	def list_notes_in_octave(self, octave):
		new_list = []
		for key, value in self.chords_in_mode('ionian').items():
			for chord in value:
				if chord[octave] not in new_list:
					new_list.append(chord[octave])
		new_list.sort()
		return new_list

	# RETURNS DICT
	def chords_in_mode(self, modename):
		return self.raw_modal_database[modename]['chords']

	def chords_in_octave(self, octave):
		new_dict = {}
		for key, value in self.chords.items():
			new_dict[key] = [i[octave] for i in self.chords[key]]
		return new_dict

	def chords_in_modal_octave(self, modename, octave):
		new_dict = {}
		for key, value in self.raw_modal_database[modename]['chords'].items():
			new_dict[key] = [i[octave] for i in value]
		return new_dict

def list_mode_names():
	return [
		'ionian',
		'dorian',
		'phrygian',
		'lydian',
		'mixolydian',
		'aeolian',
		'locrian'
	]

def list_note_names():
	return [
		'As',
		'A',
		'B',
		'Cs',
		'C',
		'Ds',
		'D',
		'E',
		'Es',
		'Fs',
		'F',
		'Gs',
		'G',
		'Ab',
		'Bb',
		'Db',
		'Eb',
		'Gb'
	]

def list_key_names():
        return [
		'a_major',
		'a_minor',
		'b_major',
		'b_minor',
		'c_major',
		'c_minor',
		'd_major',
		'd_minor',
		'e_major',
		'e_minor',
		'f_major',
		'f_minor',
		'g_major',
		'g_minor'
	]

