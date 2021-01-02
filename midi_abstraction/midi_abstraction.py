#!/usr/bin/env python3

class Notes:
	def __init__(self):
		self.As = [i * 12 + 10 for i in range(0, 10)]
		self.A = [i * 12 + 9 for i in range(0, 10)]
		self.Ab = [i * 12 + 8 for i in range(0, 10)]
		self.B = [i * 12 + 11 for i in range(0, 10)]
		self.Bb = [i * 12 + 10 for i in range(0, 10)]
		self.Cs = [i * 12 + 1 for i in range(0, 11)]
		self.C = [i * 12 for i in range(0, 11)]
		self.Ds = [i * 12 + 3 for i in range(0, 11)]
		self.D = [i * 12 + 2 for i in range(0, 11)]
		self.Db = [i * 12 + 1 for i in range(0, 11)]
		self.E = [i * 12 + 4 for i in range(0, 11)]
		self.Eb = [i * 12 + 3 for i in range(0, 11)]
		self.Fs = [i * 12 + 6 for i in range(0, 11)]
		self.F = [i * 12 + 5 for i in range(0, 11)]
		self.Gs = [i * 12 + 8 for i in range(0, 10)]
		self.G = [i * 12 + 7 for i in range(0, 11)]
		self.Gb = [i * 12 + 6 for i in range(0, 11)]

class Key:
	def __init__(self, name):

		# initialize our notes
		notes = Notes()

		self.name = name

		# get our chords from key
		if name == 'a_major':
			self.chords = {
				'a_major': [notes.A, notes.Cs, notes.E],
				'a_major_seventh': [notes.A, notes.Cs, notes.E, notes.Gs],
				'b_minor': [notes.B, notes.D, notes.Fs],
				'b_minor_seventh': [notes.B, notes.D, notes.Fs, notes.A],
				'cs_minor': [notes.Cs, notes.E, notes.Gs],
				'cs_minor_seventh': [notes.Cs, notes.E, notes.Gs, notes.B],
				'd_major': [notes.D, notes.Fs, notes.A],
				'd_major_seventh': [notes.D, notes.Fs, notes.A, notes.Cs],
				'e_major': [notes.E, notes.Gs, notes.B],
				'e_dom_seventh': [notes.E, notes.Gs, notes.B, notes.D],
				'fs_minor': [notes.Fs, notes.A, notes.Cs],
				'fs_minor_seventh': [notes.Fs, notes.A, notes.Cs, notes.E],
				'gs_dim': [notes.Gs, notes.B, notes.D],
				'gs_minor_seventh_flat_five': [notes.Gs, notes.B, notes.D, notes.Fs]
			}
		elif name == 'a_minor':
			self.chords = {
				'a_minor': [notes.A, notes.C, notes.E],
				'a_minor_seventh': [notes.A, notes.C, notes.E, notes.G],
				'b_dim': [notes.B, notes.D, notes.F],
				'b_minor_seventh_flat_five': [notes.B, notes.D, notes.F, notes.A],
				'c_major': [notes.C, notes.E, notes.G],
				'c_major_seventh': [notes.C, notes.E, notes.G, notes.B],
				'd_minor': [notes.D, notes.F, notes.A],
				'd_minor_seventh': [notes.D, notes.F, notes.A, notes.C],
				'e_minor': [notes.E, notes.G, notes.B],
				'e_minor_seventh': [notes.E, notes.G, notes.B, notes.D],
				'f_major': [notes.F, notes.A, notes.C],
				'f_major_seventh': [notes.F, notes.A, notes.C, notes.E],
				'g_major': [notes.G, notes.B, notes.D],
				'g_dom_seventh': [notes.G, notes.B, notes.D, notes.F]
			}
		elif name == 'b_major':
			self.chords = {
				'b_major': [notes.B, notes.Ds, notes.Fs],
				'b_major_seventh': [notes.B, notes.Ds, notes.Fs, notes.As],
				'cs_minor': [notes.Cs, notes.E, notes.Gs],
				'cs_minor_seventh': [notes.Cs, notes.E, notes.Gs, notes.B],
				'ds_minor': [notes.Ds, notes.Fs, notes.As],
				'ds_minor_seventh': [notes.Ds, notes.Fs, notes.As, notes.Cs],
				'e_major': [notes.E, notes.Gs, notes.B],
				'e_major_seventh': [notes.E, notes.Gs, notes.B, notes.Ds],
				'fs_major': [notes.Fs, notes.As, notes.Cs],
				'fs_dom_seventh': [notes.Fs, notes.As, notes.Cs, notes.E],
				'gs_minor': [notes.Gs, notes.B, notes.Ds],
				'gs_minor_seventh': [notes.Gs, notes.B, notes.Ds, notes.Fs],
				'as_dim': [notes.As, notes.Cs, notes.E],
				'as_minor_seventh_flat_five': [notes.As, notes.Cs, notes.E, notes.Gs]
			}
		elif name == 'b_minor':
			self.chords = {
				'b_minor': [notes.B, notes.D, notes.Fs],
				'b_minor_seventh': [notes.B, notes.D, notes.Fs, notes.A],
				'cs_dim': [notes.Cs, notes.E, notes.G],
				'cs_minor_seventh_flat_five': [notes.Cs, notes.E, notes.G, notes.B],
				'd_major': [notes.D, notes.Fs, notes.A],
				'd_major_seventh': [notes.D, notes.Fs, notes.A, notes.Cs],
				'e_minor': [notes.E, notes.G, notes.B],
				'e_minor_seventh': [notes.E, notes.G, notes.B, notes.D],
				'fs_minor': [notes.Fs, notes.A, notes.Cs],
				'fs_minor_seventh': [notes.Fs, notes.A, notes.Cs, notes.E],
				'g_major': [notes.G, notes.B, notes.D],
				'g_major_seventh': [notes.G, notes.B, notes.D, notes.Fs],
				'a_major': [notes.A, notes.Cs, notes.E],
				'a_dom_seventh': [notes.A, notes.Cs, notes.E, notes.G]
			}
		elif name == 'c_major':
			self.chords = {
				'c_major': [notes.C, notes.E, notes.G],
				'c_major_seventh': [notes.C, notes.E, notes.G, notes.B],
				'd_minor': [notes.D, notes.F, notes.A],
				'd_minor_seventh': [notes.D, notes.F, notes.A, notes.C],
				'e_minor': [notes.E, notes.G, notes.B],
				'e_minor_seventh': [notes.E, notes.G, notes.B, notes.D],
				'f_major': [notes.F, notes.A, notes.C],
				'f_major_seventh': [notes.F, notes.A, notes.C, notes.E],
				'g_major': [notes.G, notes.B, notes.D],
				'g_major_seventh': [notes.G, notes.B, notes.D, notes.F],
				'a_minor': [notes.A, notes.C, notes.E],
				'a_minor_seventh': [notes.A, notes.C, notes.E, notes.G],
				'b_dim': [notes.B, notes.D, notes.F],
				'b_minor_seventh_flat_five': [notes.B, notes.D, notes.F, notes.A]
			}
		elif name == 'c_minor':
			self.chords = {
				'c_minor': [notes.C, notes.Eb, notes.G],
				'c_minor_seventh': [notes.C, notes.Eb, notes.G, notes.Bb],
				'd_dim': [notes.D, notes.F, notes.Ab],
				'd_minor_seventh_flat_five': [notes.D, notes.F, notes.Ab, notes.C],
				'eb_major': [notes.Eb, notes.G, notes.Bb],
				'eb_major_seventh': [notes.Eb, notes.G, notes.Bb, notes.D],
				'f_minor': [notes.F, notes.Ab, notes.C],
				'f_minor_seventh': [notes.F, notes.Ab, notes.C, notes.Eb],
				'g_minor': [notes.G, notes.Bb, notes.D],
				'g_minor_seventh': [notes.G, notes.Bb, notes.D, notes.F],
				'ab_major': [notes.Ab, notes.C, notes.Eb],
				'ab_major_seventh': [notes.Ab, notes.C, notes.Eb, notes.G],
				'bb_major': [notes.Bb, notes.D, notes.F],
				'bb_dom_seventh': [notes.Bb, notes.D, notes.F, notes.Ab]
			}
		elif name == 'd_major':
			self.chords = {
				'd_major': [notes.D, notes.Fs, notes.A], 
				'd_major_seventh': [notes.D, notes.Fs, notes.A, notes.Cs],
				'e_minor': [notes.E, notes.G, notes.B], 
				'e_minor_seventh': [notes.E, notes.G, notes.B, notes.D],
				'fs_minor': [notes.Fs, notes.A, notes.Cs],
				'fs_minor_seventh': [notes.Fs, notes.A, notes.Cs, notes.E],
				'g_major': [notes.G, notes.B, notes.D], 
				'g_major_seventh': [notes.G, notes.B, notes.D, notes.Fs],
				'a_major': [notes.A, notes.Cs, notes.E],
				'a_dom_seventh': [notes.A, notes.Cs, notes.E, notes.G],
				'b_minor': [notes.B, notes.D, notes.Fs],
				'b_minor_seventh': [notes.B, notes.D, notes.Fs, notes.A],
				'cs_dim': [notes.Cs, notes.E, notes.G],
				'cs_minor_seventh_flat_five': [notes.Cs, notes.E, notes.G, notes.B]
			}
		elif name == 'd_minor':
			self.chords = {
				'd_minor': [notes.D, notes.F, notes.A],
				'd_minor_seventh': [notes.D, notes.F, notes.A, notes.C],
				'e_dim': [notes.E, notes.G, notes.Bb],
				'e_minor_seventh_flat_five': [notes.E, notes.G, notes.Bb, notes.D],
				'f_major': [notes.F, notes.A, notes.C],
				'f_major_seventh': [notes.F, notes.A, notes.C, notes.E],
				'g_minor': [notes.G, notes.Bb, notes.D],
				'g_minor_seventh': [notes.G, notes.Bb, notes.D, notes.F],
				'a_minor': [notes.A, notes.C, notes.E],
				'a_minor_seventh': [notes.A, notes.C, notes.E, notes.G],
				'bb_major': [notes.Bb, notes.D, notes.F],
				'bb_major_seventh': [notes.Bb, notes.D, notes.F, notes.A],
				'c_major': [notes.C, notes.E, notes.G],
				'c_dom_seventh': [notes.C, notes.E, notes.G, notes.Bb]
			}
		elif name == 'e_major':
			self.chords = {
				'e_major': [notes.E, notes.Gs, notes.B],
				'e_major_seventh': [notes.E, notes.Gs, notes.B, notes.Ds],
				'fs_minor': [notes.Fs, notes.A, notes.Cs],
				'fs_minor_seventh': [notes.Fs, notes.A, notes.Cs, notes.E],
				'gs_minor': [notes.Gs, notes.B, notes.Ds],
				'gs_minor_seventh': [notes.Gs, notes.B, notes.Ds, notes.Fs],
				'a_major': [notes.A, notes.Cs, notes.E],
				'a_major_seventh': [notes.A, notes.Cs, notes.E, notes.Gs],
				'b_major': [notes.B, notes.Ds, notes.Fs],
				'b_dom_seventh': [notes.B, notes.Ds, notes.Fs, notes.A],
				'cs_minor': [notes.Cs, notes.E, notes.Gs],
				'cs_minor_seventh': [notes.Cs, notes.E, notes.Gs, notes.B],
				'ds_dim': [notes.Ds, notes.Fs, notes.A],
				'ds_minor_seventh_flat_five': [notes.Ds, notes.Fs, notes.A, notes.Cs]
			}
		elif name == 'e_minor':
			self.chords = {
				'e_minor': [notes.E, notes.G, notes.B],
				'e_minor_seventh': [notes.E, notes.G, notes.B, notes.D],
				'fs_dim': [notes.Fs, notes.A, notes.C],
				'fs_minor_seventh_flat_five': [notes.Fs, notes.A, notes.C, notes.E],
				'g_major': [notes.G, notes.B, notes.D],
				'g_major_seventh': [notes.G, notes.B, notes.D, notes.Fs],
				'a_minor': [notes.A, notes.C, notes.E],
				'a_minor_seventh': [notes.A, notes.C, notes.E, notes.G],
				'b_minor': [notes.B, notes.D, notes.F],
				'b_minor_seventh': [notes.B, notes.D, notes.Fs, notes.A],
				'c_major': [notes.C, notes.E, notes.G],
				'c_major_seventh': [notes.C, notes.E, notes.G, notes.B],
				'd_major': [notes.D, notes.Fs, notes.A],
				'd_dom_seventh': [notes.D, notes.Fs, notes.A, notes.C]
			}
		elif name == 'f_major':
			self.chords = {
				'f_major': [notes.F, notes.A, notes.C],
				'f_major_seventh': [notes.F, notes.A, notes.C, notes.E],
				'g_minor': [notes.G, notes.Bb, notes.D],
				'g_minor_seventh': [notes.G, notes.Bb, notes.D, notes.F],
				'a_minor': [notes.A, notes.C, notes.E],
				'a_minor_seventh': [notes.A, notes.C, notes.E, notes.G],
				'bb_major': [notes.Bb, notes.D, notes.F],
				'bb_major_seventh': [notes.Bb, notes.D, notes.F, notes.A],
				'c_major': [notes.C, notes.E, notes.G],
				'c_dom_seventh': [notes.C, notes.E, notes.G, notes.Bb],
				'd_minor': [notes.D, notes.F, notes.A],
				'd_minor_seventh': [notes.D, notes.F, notes.A, notes.C],
				'e_dim': [notes.E, notes.G, notes.Bb],
				'e_minor_seventh_flat_five': [notes.E, notes.G, notes.Bb, notes.D]
			}
		elif name == 'f_minor':
			self.chords = {
				'f_minor': [notes.F, notes.Ab, notes.C],
				'f_minor_seventh': [notes.F, notes.Ab, notes.C, notes.Eb],
				'g_dim': [notes.G, notes.Bb, notes.Db],
				'g_minor_seventh_flat_five': [notes.G, notes.Bb, notes.Db, notes.F],
				'ab_major': [notes.Ab, notes.C, notes.Eb],
				'ab_major_seventh': [notes.Ab, notes.C, notes.Eb, notes.G],
				'bb_minor': [notes.Bb, notes.Db, notes.F],
				'bb_minor_seventh': [notes.Bb, notes.Db, notes.F, notes.Ab],
				'c_minor': [notes.C, notes.Eb, notes.G],
				'c_minor_seventh': [notes.C, notes.Eb, notes.G, notes.Bb],
				'db_major': [notes.Db, notes.F, notes.Ab],
				'db_major_seventh': [notes.Db, notes.F, notes.Ab, notes.C],
				'eb_major': [notes.Eb, notes.G, notes.Bb],
				'eb_dom_seventh': [notes.Eb, notes.G, notes.Bb, notes.Db]
			}
		elif name == 'g_major':
			self.chords = {
				'g_major': [notes.G, notes.B, notes.D],
				'g_major_seventh': [notes.G, notes.B, notes.D, notes.Fs],
				'a_minor': [notes.A, notes.C, notes.E],
				'a_minor_seventh': [notes.A, notes.C, notes.E, notes.G],
				'b_minor': [notes.B, notes.D, notes.Fs],
				'b_minor_seventh': [notes.B, notes.D, notes.Fs, notes.A],
				'c_major': [notes.C, notes.E, notes.G],
				'c_major_seventh': [notes.C, notes.E, notes.G, notes.B],
				'd_major': [notes.D, notes.Fs, notes.A],
				'd_dom_seventh': [notes.D, notes.Fs, notes.A, notes.C],
				'e_minor': [notes.E, notes.G, notes.B],
				'e_minor_seventh': [notes.E, notes.G, notes.B, notes.D],
				'fs_dim': [notes.Fs, notes.A, notes.C],
				'fs_minor_seventh_flat_five': [notes.Fs, notes.A, notes.C, notes.E] 
			}
		elif name == 'g_minor':
			self.chords = {
				'g_minor': [notes.G, notes.Bb, notes.D],
				'g_minor_seventh': [notes.G, notes.Bb, notes.D, notes.F],
				'a_dim': [notes.A, notes.C, notes.Eb],
				'a_minor_seventh_flat_five': [notes.A, notes.C, notes.Eb, notes.G],
				'bb_major': [notes.Bb, notes.D, notes.F],
				'bb_major_seventh': [notes.Bb, notes.D, notes.F, notes.A],
				'c_minor': [notes.C, notes.Eb, notes.G],
				'c_minor_seventh': [notes.C, notes.Eb, notes.G, notes.Bb],
				'd_minor': [notes.D, notes.F, notes.A],
				'd_minor_seventh': [notes.D, notes.F, notes.A, notes.C],
				'eb_major': [notes.Eb, notes.G, notes.Bb],
				'eb_major_seventh': [notes.Eb, notes.G, notes.Bb, notes.D],
				'f_major': [notes.F, notes.A, notes.C],
				'f_dom_seventh': [notes.F, notes.A, notes.C, notes.Eb]
			}
		else:
			raise NameError(f'{name} is not a valid musical key or is not defined as such in {__file__}')


	def chords_in_octave(self, octave):
		new_dict = {}
		for key, value in self.chords.items():
			new_dict[key] = [i[octave] for i in self.chords[key]]

		return new_dict

	def diatonic_chords(self):
		new_dict = {}
		if 'major' in self.name:
			diatonics = [i for i in self.chords if 'seventh' not in i and 'dim' not in i]
		else:
			diatonics = [i for i in self.chords if 'seventh' not in i]
		for i in diatonics:
			if i in self.chords.keys():
				new_dict[i] = self.chords[i]
		return new_dict

	def diatonic_chords_in_octave(self, octave):
		diatonics = self.diatonic_chords()
		new_dict = {}
		for key, value in diatonics.items():
			new_dict[key] = [i[octave] for i in value]
		return new_dict

	def notes_in_octave(self, octave):
		chords = self.chords_in_octave(octave)
		notes = []
		for lst in chords.values():
			for note in lst:
				if note not in notes:
					notes.append(note)
		return sorted(notes)

	def notes_in_key(self):
		chords = self.chords.values()
		unique_notes = []
		for lst in chords:
			for notes in lst:
				for note in notes:
					if note not in unique_notes:
						unique_notes.append(note)
		return sorted(unique_notes)

	def chords_in_key(self):
		return self.chords

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

