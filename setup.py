import setuptools

with open('README.md', 'r', encoding = 'utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name = 'midi-abstraction',
	version = '0.8.1',
	author = 'Marco Silva',
	author_email = 'cyberrumor@gmail.com',
	description = 'Abstract MIDI pitches into keys, chords and notes.',
	long_description_content_type = 'text/markdown',
	url = 'https://github.com/cyberrumor/midi_abstraction',
	packages = setuptools.find_packages(),
	classifiers = [
		'Programming Language :: Python :: 3.9',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Operating System :: OS Independent',
	],
	python_requires = '>=3.9',
)
