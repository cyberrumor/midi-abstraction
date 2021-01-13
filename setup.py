import setuptools

with open('README.md', 'r', encoding = 'utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name = 'midi-abstraction',
	version = '0.9.7',
	author = 'Marco Silva',
	author_email = 'cyberrumor@gmail.com',
	description = 'Abstract MIDI pitches into keys, chords, modes, notes, and octaves.',
	long_description_content_type = 'text/markdown',
	long_description = long_description,
	url = 'https://github.com/cyberrumor/midi_abstraction',
	packages = ['midi_abstraction'],
	classifiers = [
		'Programming Language :: Python :: 3.9',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Operating System :: OS Independent',
	],
	python_requires = '>=3.9',
)

