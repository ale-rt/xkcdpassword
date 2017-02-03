#!/usr/bin/env python

from random import choice
import argparse, sys

parser = argparse.ArgumentParser(description='Generate an XKCD-style password.')
parser.add_argument('words', metavar='n', nargs='?', type=int, default=4, help='Number of words to produce (default = 4)', choices=range(1,20))
parser.add_argument('-ns', help='Remove spaces for copy-pasting or piping', action='store_true')

words = []

with open('words.txt', 'r') as tempfile:
	words = [a.strip() for a in tempfile.readlines()]
	
def randwords(num): 
	'''Generates random words from the provided text file
	and ensures uniqueness.'''
	indset = set()
	while len(indset) < num:
		indset.add(choice(words))
	return list(indset)
	
if __name__ == "__main__":
	args = parser.parse_args()
	sys.stdout.write(('' if args.ns else ' ').join(randwords(args.words))+'\n')
