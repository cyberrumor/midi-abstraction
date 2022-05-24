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

	if type(name) == str:
		return note_dict[name.lower()]

	elif type(name) == int:
		if name <= 127 and name >= 0:
			for key, value in note_dict.items():
				if name in value:
					return key
		else:
			raise ValueError(f'{name} is not in range(0, 127). Therefor, it can\'t be converted into a note name.')
	else:
		raise TypeError(f'{name} is not a type of int or str, so it can\'t be converted into a note name or midi pitch.')

def drums_dict():
	drum_dict = {
		'acoustic_base_drum': 35,
		'bass_drum_1': 36,
		'side_stick': 37,
		'acoustic_snare': 38,
		'hand_clap': 39,
		'electric_snare': 40,
		'low_floor_tom': 41,
		'closed_hi_hat': 42,
		'high_floor_tom': 43,
		'pedal_hi_hat': 44,
		'low_tom': 45,
		'open_hi_hat': 46,
		'low_mid_tom': 47,
		'hi_mid_tom': 48,
		'crash_cymbal_1': 49,
		'high_tom': 50,
		'ride_cymbal_1': 51,
		'chinese_cymbal': 52,
		'ride_bell': 53,
		'tambourine': 54,
		'splash_cymbal': 55,
		'cowbell': 56,
		'crash_cymbal_2': 57,
		'vibraslap': 58,
		'ride_cymbal_2': 59,
		'hi_bongo': 60,
		'low_bongo': 61,
		'mute_hi_conga': 62,
		'open_hi_conga': 63,
		'low_conga': 64,
		'high_timbale': 65,
		'low_timbale': 66,
		'high_agogo': 67,
		'low_agogo': 68,
		'cabasa': 69,
		'maracas': 70,
		'short_whistle': 71,
		'long_whistle': 72,
		'short_guiro': 73,
		'long_guiro': 74,
		'claves': 75,
		'hi_wood_block': 76,
		'low_wood_block': 77,
		'mute_cuica': 78,
		'open_cuica': 79,
		'mute_triangle': 80,
		'open_triangle': 81
	}
	return drum_dict

def drums(name):
	drum_dict = drums_dict()
	if type(name) == str:
		return drum_dict[name.lower()]
	elif type(name) == int:
		if name >= 35 and name <= 81:
			for key, value in drum_dict.items():
				if name == value:
					return key
		else:
			raise ValueError(f'{name} is not in range(35, 81), therefor it can\'t be converted into a drum name.')
	else:
		raise TypeError(f'{name} is not a type of int or str, so it can\'t be converted into a drum name or midi pitch.')


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

def relative_chord_dict():
	chord_dict = {
			'c_major': 'a_minor',
			'g_major': 'e_minor',
			'd_major': 'b_minor',
			'a_major': 'fs_minor',
			'e_major': 'cs_minor',
			'b_major': 'gs_minor',
			'fs_major': 'ds_minor',
			'cs_major': 'as_minor',
			'f_major': 'd_minor',
			'bb_major': 'g_minor',
			'eb_major': 'c_minor',
			'ab_major': 'f_minor',
			'db_major': 'bb_minor',
			'gb_major': 'eb_minor',
			'cb_major': 'ab_minor',
			'a_minor': 'c_major',
			'e_minor': 'g_major',
			'b_minor': 'd_major',
			'fs_minor': 'a_major',
			'cs_minor': 'e_major',
			'gs_minor': 'b_major',
			'ds_minor': 'fs_major',
			'as_minor': 'cs_major',
			'd_minor': 'f_major',
			'g_minor': 'bb_major',
			'c_minor': 'eb_major',
			'f_minor': 'ab_major',
			'bb_minor': 'db_major',
			'eb_minor': 'gb_major',
			'ab_minor': 'cb_major',
	}
	return chord_dict

def relative_chord_name(name):
	chord_dict = relative_chord_dict()
	if has_relative_chord(name):
		return chord_dict[name]
	raise KeyError(f'{name} has no relative chord. You can test this with has_relative_chord({name})')

def has_relative_chord(name):
	if name in relative_chord_dict().keys():
		return True
	return False

def relative_chord(name):
	if has_relative_chord(name):
		return chords(relative_chord_name(name))
	raise KeyError(f'{name} has no relative chord. You can test this with has_relative_chord({name})')

class Key:
	def __init__(self, name):
		self.name = name

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
				root = universe().index(''.join(name[0:2]))
			# in universe(), we only have sharps, so we need to convert flats to sharps by
			# traversing backwards through the index by 1 to get the correct sharp.
			elif name[1].lower() == 'b':
				root = universe().index(name[0]) - 1
				if root == -1:
					root = 12
				print(f'root: {root}')
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

		self.relative_key = relative_chord_name(self.name)

	# RETURNS LISTS
	def list_notes(self):
		return [i for i in list(self.notes.keys())]

	def list_chords(self):
		return [i for i in list(self.chords.keys())]

	# this tries to get a relative chord for each chord in the current key.
	# excludes dim, sus, or any other chord that I haven't programmed relative
	# support for yet.
	def list_relative_chords(self):
		return [relative_chord_name(i) for i in list(self.chords.keys()) if has_relative_chord(i)]

	# this takes the relative key, and lists all chords in it.
	def list_chords_in_relative_key(self):
		if has_relative_chord(self.name):
			return Key(self.relative_key).list_chords()
		raise KeyError(f"{self.name} doesn't support relative chords yet.")


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
