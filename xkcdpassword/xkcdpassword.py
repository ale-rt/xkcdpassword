#!/usr/bin/env python

import argparse, sys, random, os, pyperclip
from os.path import join, dirname, realpath

localpath = dirname(realpath(__file__))

parser = argparse.ArgumentParser(description='Generate an XKCD-style password.')
parser.add_argument('words', nargs='?', type=int, default=4, help='Number of words to produce (default = 4)', choices=range(1,21))
parser.add_argument('-c', '--clip', help='Send result to clipboard rather than sys.stdout', action='store_true')
parser.add_argument('-n', '--nospaces', help='Don\'t separate the output passphrase with spaces; Overrides delimiter option', action='store_true')
parser.add_argument('-e', '--easywords', help='Use a dictionary of more common words', action='store_true')
parser.add_argument('-s', '--seed', help='Seed for random function, if you want predictable results', action='store')
parser.add_argument('-d', '--delimiter', type=str, default=' ', help='Custome character or string to split words', action='store')
parser.add_argument('-f', '--dictionaryfile', type=str, default=join(localpath, 'words.txt'), help='Absolute path to an alternative dictionary', action='store')

def randwords(num, inseed, fn): 
	'''Generates random words from the provided text file
	and ensures uniqueness.'''
	words = []
	numlines = 0
	with open(fn, 'r') as tempfile:
		numlines = sum([1 for x in tempfile])
	with open(fn, 'r') as tempfile:
		indices = []
		if inseed:
			random.seed(inseed)
		while len(indices) < num:
			ind = random.randint(0, numlines - 1)
			if ind not in indices:
				indices.append(ind)
		lines = tempfile.readlines()
		words = [lines[a].strip() for a in indices]
	return words
	
def main():
	'''Primary entry point'''
	args = parser.parse_args()
	fn = join(localpath, 'easywords.txt') if args.easywords else args.dictionaryfile
	rwords = randwords(args.words, args.seed, fn)
	outstr = ('' if args.nospaces else args.delimiter).join(rwords)
	if args.clip:
		pyperclip.copy(outstr)
	else:
		sys.stdout.write(outstr)
		sys.stdout.write('\n')
	
if __name__ == "__main__":
	main()
