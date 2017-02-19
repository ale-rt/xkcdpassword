#!/usr/bin/env python

from setuptools import setup

install_requires = ['pyperclip']

setup(
	name = 'xkcdpassword',
	packages = ['xkcdpassword'],
	data_files = [('xkcdpassword',['xkcdpassword/words.txt','xkcdpassword/oldwords.txt'])],
	version = '0.6.3',
	description = 'A generator of xkcd-style passwords',
	author = 'Doug Walter',
	author_email = 'dougwritescode@gmail.com',
	url = 'https://github.com/dougwritescode/xkcdpassword',
	download_url = 'https://github.com/dougwritescode/xkcdpassword/tarball/0.6.3', 
	keywords = 'python xkcd utilities security password', 
	classifiers = ['Development Status :: 3 - Alpha',
		'Environment :: Console',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Programming Language :: Python :: 2.7',
		'Topic :: Security',
		'Topic :: Utilities',],
	entry_points = {
		'console_scripts': [
            'xkcdpassword = xkcdpassword.xkcdpassword:main',
        ],
        'gui_scripts': []
	},
)
