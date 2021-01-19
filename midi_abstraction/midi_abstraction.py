#!/usr/bin/env python3

def list_modes():
	return [
		'ionian',
		'dorian',
		'phrygian',
		'lydian',
		'mixolydian',
		'aeolian',
		'locrian'
	]


def universe():
        return ['a', 'as', 'b', 'c', 'cs', 'd', 'ds', 'e', 'f', 'fs', 'g', 'gs'] * 2

def list_notes():
	result = []
	for i in universe():
		if i not in result:
			result.append(i)
	return result

def list_keys():
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

def notes(name):
	if type(name) != str:
		raise TypeError(f'midi_abstraction.notes({name}) was fed a {type(name)} but expected a string.')
	note_dict = {
		'as': [i * 12 + 10 for i in range(0, 10)],
		'a': [i * 12 + 9 for i in range(0, 10)],
		'b': [i * 12 + 11 for i in range(0, 10)],
		'cs': [i * 12 + 1 for i in range(0, 11)],
		'c': [i * 12 for i in range(0, 11)],
		'ds': [i * 12 + 3 for i in range(0, 11)],
		'd': [i * 12 + 2 for i in range(0, 11)],
		'e': [i * 12 + 4 for i in range(0, 11)],
		'es': [i * 12 + 5 for i in range(0, 11)],
		'fs': [i * 12 + 6 for i in range(0, 11)],
		'f': [i * 12 + 5 for i in range(0, 11)],
		'gs': [i * 12 + 8 for i in range(0, 10)],
		'g': [i * 12 + 7 for i in range(0, 11)],
		'ab': [i * 12 + 8 for i in range(0, 10)],
		'bb': [i * 12 + 10 for i in range(0, 10)],
		'db': [i * 12 + 1 for i in range(0, 11)],
		'eb': [i * 12 + 3 for i in range(0, 11)],
		'gb': [i * 12 + 6 for i in range(0, 11)]
	}
	return note_dict[name.lower()]

def chords(name):
	chord_dict = {
		'a_minor': [notes('a'), notes('c'), notes('e')],
		'a_minor_seventh': [notes('a'), notes('c'), notes('e'), notes('g')],
		'as_dim': [notes('as'), notes('cs'), notes('e')],
		'as_minor_seventh_flat_five': [notes('as'), notes('cs'), notes('e'), notes('gs')],
		'as_major': [notes('as'), notes('d'), notes('f')],
		'as_minor': [notes('as'), notes('cs'), notes('es')],
		'a_major': [notes('a'), notes('cs'), notes('e')],
		'a_dim': [notes('a'), notes('c'), notes('eb')],
		'a_major_seventh': [notes('a'), notes('cs'), notes('e'), notes('gs')],
		'a_dom_seventh': [notes('a'), notes('cs'), notes('e'), notes('g')],
		'ab_major': [notes('ab'), notes('c'), notes('eb')],
		'ab_major_seventh': [notes('ab'), notes('c'), notes('eb'), notes('g')],
		'bb_major_seventh': [notes('bb'), notes('d'), notes('f'), notes('a')],
		'bb_major': [notes('bb'), notes('d'), notes('f')],
		'bb_dom_seventh': [notes('bb'), notes('d'), notes('f'), notes('ab')],
		'b_dim': [notes('b'), notes('d'), notes('f')],
		'b_minor_seventh_flat_five': [notes('b'), notes('d'), notes('f'), notes('a')],
		'b_major': [notes('b'), notes('ds'), notes('fs')],
		'b_major_seventh': [notes('b'), notes('ds'), notes('fs'), notes('as')],
		'b_minor': [notes('b'), notes('d'), notes('fs')],
		'b_minor_seventh': [notes('b'), notes('d'), notes('fs'), notes('a')],
		'cs_dim': [notes('cs'), notes('e'), notes('g')],
		'cs_major': [notes('cs'), notes('f'), notes('g')],
		'cs_minor_seventh_flat_five': [notes('cs'), notes('e'), notes('g'), notes('b')],
		'cs_minor': [notes('cs'), notes('e'), notes('gs')],
		'cs_minor_seventh': [notes('cs'), notes('e'), notes('gs'), notes('b')],
		'c_major': [notes('c'), notes('e'), notes('g')],
		'c_dim': [notes('c'), notes('eb'), notes('gb')],
		'c_major_seventh': [notes('c'), notes('e'), notes('g'), notes('b')],
		'c_minor': [notes('c'), notes('eb'), notes('g')],
		'c_minor_seventh': [notes('c'), notes('eb'), notes('g'), notes('bb')],
		'c_dom_seventh': [notes('c'), notes('e'), notes('g'), notes('bb')],
		'ds_major': [notes('ds'), notes('g'), notes('as')],
		'ds_dim': [notes('ds'), notes('fs'), notes('a')],
		'ds_minor': [notes('ds'), notes('fs'), notes('as')],
		'ds_minor_seventh': [notes('ds'), notes('fs'), notes('as'), notes('cs')],
		'd_major': [notes('d'), notes('fs'), notes('a')],
		'd_major_seventh': [notes('d'), notes('fs'), notes('a'), notes('cs')],
		'd_minor': [notes('d'), notes('f'), notes('a')],
		'd_minor_seventh': [notes('d'), notes('f'), notes('a'), notes('c')],
		'd_dim': [notes('d'), notes('f'), notes('ab')],
		'd_minor_seventh_flat_five': [notes('d'), notes('f'), notes('ab'), notes('c')],
		'e_major': [notes('e'), notes('gs'), notes('b')],
		'e_major_seventh': [notes('e'), notes('gs'), notes('b'), notes('ds')],
		'e_dom_seventh': [notes('e'), notes('gs'), notes('b'), notes('d')],
		'e_minor': [notes('e'), notes('g'), notes('b')],
		'e_minor_seventh': [notes('e'), notes('g'), notes('b'), notes('d')],
		'eb_major': [notes('eb'), notes('g'), notes('bb')],
		'eb_major_seventh': [notes('eb'), notes('g'), notes('bb'), notes('d')],
		'e_dim': [notes('e'), notes('g'), notes('bb')],
		'e_minor_seventh_flat_five': [notes('e'), notes('g'), notes('bb'), notes('d')],
		'fs_minor': [notes('fs'), notes('a'), notes('cs')],
		'fs_minor_seventh': [notes('fs'), notes('a'), notes('cs'), notes('e')],
		'f_major': [notes('f'), notes('a'), notes('c')],
		'f_dim': [notes('f'), notes('ab'), notes('b')],
		'f_major_seventh': [notes('f'), notes('a'), notes('c'), notes('e')],
		'fs_major': [notes('fs'), notes('as'), notes('cs')],
		'fs_dim': [notes('fs'), notes('a'), notes('c')],
		'fs_dom_seventh': [notes('fs'), notes('as'), notes('cs'), notes('e')],
		'f_minor': [notes('f'), notes('ab'), notes('c')],
		'gs_major': [notes('gs'), notes('c'), notes('ds')],
		'gs_minor': [notes('gs'), notes('b'), notes('ds')],
		'gs_minor_seventh': [notes('gs'), notes('b'), notes('ds'), notes('fs')],
		'gs_dim': [notes('gs'), notes('b'), notes('d')],
		'gs_minor_seventh_flat_five': [notes('gs'), notes('b'), notes('d'), notes('fs')],
		'g_major': [notes('g'), notes('b'), notes('d')],
		'g_dim': [notes('g'), notes('bb'), notes('db')],
		'g_dom_seventh': [notes('g'), notes('b'), notes('d'), notes('f')],
		'g_major_seventh': [notes('g'), notes('b'), notes('d'), notes('fs')],
		'g_minor': [notes('g'), notes('bb'), notes('d')],
		'g_minor_seventh': [notes('g'), notes('bb'), notes('d'), notes('f')]

	}
	if name in list(chord_dict.keys()):
		return chord_dict[name]
	else:
		result = []
		makeshift_name = name.split('_')
		for i in makeshift_name:
			result.append(notes(i))
		return result

class Key:
	def __init__(self, name):
		self.name = name
		# universe = ['a', 'as', 'b', 'c', 'cs', 'd', 'ds', 'e', 'f', 'fs', 'g', 'gs'] * 2
		W = 2
		H = 1
		default_mode = [W, W, H, W, W, W, H]

		locrian = [default_mode[6]] + default_mode[0:6]
		mixolydian = default_mode[4:] + default_mode[0:4]
		lydian = default_mode[3:] + default_mode[0:3]
		phrygian = default_mode[2:] + default_mode[0:2]
		dorian = default_mode[1:] + [default_mode[0]]
		ionian = default_mode
		aeolian = default_mode[5:] + default_mode[0:5]
		major = default_mode
		minor = aeolian

		mode_structures = {
				'ionian': ionian,
				'dorian': dorian,
				'phrygian': phrygian,
				'lydian': lydian,
				'mixolydian': mixolydian,
				'aeolian': aeolian,
				'locrian': locrian,
				'major': major,
				'minor': minor
		}

		if name[0].lower() in universe():
			if name[1] == '_':
				root = universe().index(name[0])
			elif name[1].lower() == 's':
				root = universe().index(''.join(name[0:3]))
			elif name[1].lower() == 'b':
				check = universe().index(name[0]) - 1
				root = universe().index(check)
			else:
				raise NameError(f'{name} is not a valid musical key.')
		else:
			raise NameError(f'{name} is not a valid musical key.')

		if name.split('_')[1].lower() == 'major':
			self.mode = 'ionian'
		elif name.split('_')[1].lower() == 'minor':
			self.mode = 'aeolian'
		else:
			self.mode = name.split('_')[1].lower()

		if self.mode in mode_structures:
			if self.mode in ['major', 'ionian']:
				numerals = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'viid']
				self.seniority = 'major'
			elif self.mode in ['minor', 'aeolian']:
				numerals = ['i', 'iid', 'III', 'iv', 'v', 'VI', 'VII']
				self.seniority = 'minor'
			elif self.mode == 'dorian':
				numerals = ['i', 'ii', 'III', 'IV', 'v', 'vid', 'VII']
				self.seniority = 'minor'
			elif self.mode == 'phrygian':
				numerals = ['i', 'II', 'III', 'iv', 'vd', 'VI', 'vii']
				self.seniority = 'minor'
			elif self.mode == 'lydian':
				numerals = ['I', 'II', 'iii', 'ivd', 'V', 'vi', 'vii']
				self.seniority = 'major'
			elif self.mode == 'mixolydian':
				numerals = ['I', 'ii', 'iiid', 'IV', 'v', 'vi', 'VII']
				self.seniority = 'major'
			elif self.mode == 'locrian':
				numerals = ['id', 'II', 'iii', 'iv', 'V', 'VI', 'vii']
				self.seniority = 'diminished'
		else:
			raise NameError(f'{name} is not a valid musical key.')

		slice = universe()[root:]
		index = 0
		self.chords = {}
		for step in range(len(mode_structures[self.mode])):
			if numerals[step].isupper() and 'd' not in numerals[step]:
				c = slice[index] + '_major'
			elif numerals[step].isupper() and 'd' in numerals[step]:
				c = slice[index] + '_major_dim'
			elif numerals[step].islower() and 'd' not in numerals[step]:
				c = slice[index] + '_minor'
			elif numerals[step].islower() and 'd' in numerals[step]:
				c = slice[index] + '_dim'
			else:
				raise NameError(f'{slice[index]} could not be made into a chord.')

			self.chords[c] = chords(c)
			index += mode_structures[self.mode][step]

		index = 0
		self.notes = {}
		for step in range(len(mode_structures[self.mode])):
			self.notes[slice[index]] = notes(slice[index])
			index += mode_structures[self.mode][step]

	# RETURNS LISTS
	def list_notes(self):
		return [i for i in list(self.notes.keys())]

	def list_chords(self):
		return [i for i in list(self.chords.keys())]

	def list_notes_in_octave(self, octave):
		result = []
		self_notes = self.list_notes()
		for c in self_notes:
			if notes(c)[octave] < notes(self_notes[0])[octave]:
				result.append(notes(c)[octave + 1])
			else:
				result.append(notes(c)[octave])
		return result

	def list_notes_in_pentatonic_major(self):
		pents = self.notes_in_pentatonic_major()
		return list(pents.keys())

	def list_notes_in_pentatonic_minor(self):
		pents = self.notes_in_pentatonic_minor()
		return list(pents.keys())

	# RETURNS DICTS
	def chords_in_octave(self, octave):
		new_dict = {}
		for key, value in self.chords.items():
			new_dict[key] = [i[octave] for i in self.chords[key]]
		return new_dict

	def notes_in_pentatonic_minor(self):
		# for this, we should iterate through all the possible major/minor keys until we find out which shares all the notes.
		# once we have that, we can process this more accurately.

		new_dict = {}
		if self.seniority == 'minor':
			scale = self.list_notes()
			try:
				flatted_three = universe()[universe().index(scale[2]) - 1]
			except:
				flatted_three = 'gs'
			try:
				flatted_seventh = univers()[universe().index(scale[6]) - 1]
			except:
				flatted_seventh = 'gs'

			pentatonics = [scale[0], flatted_three, scale[3], scale[4], flatted_seventh]

			for i in pentatonics:
				new_dict[i] = notes(i)

			return new_dict

		elif self.seniority == 'major':
			name = self.name
			new_name = self.name.replace(self.name.split('_')[-1], 'minor')
			k = Key(new_name)
			return k.notes_in_pentatonic_minor()

		else:
			raise NameError(f'{self.mode} does not support pentatonics yet.')

	def notes_in_pentatonic_major(self):
		# for this, we should iterate through all the possible major/minor keys until we find out which shares all notes.
		# once we have that, we can process this more accurately. 

		new_dict = {}

		if self.seniority == 'major':
			pentatonics = self.list_notes()
			pentatonics.pop(6)
			pentatonics.pop(3)
			for i in pentatonics:
				new_dict[i] = notes(i)
			return new_dict

		elif self.seniority == 'minor':
			name = self.name
			new_name = self.name.replace(self.name.split('_')[-1], 'major')
			k = Key(new_name)
			return k.notes_in_pentatonic_major()

		else:
			raise NameError(f'{self.mode} does not support pentatonics yet.')
