#! /bin/env python
# The driver module. Pulls everything together.

import sys

print "Welcome to KazAMC - Kazimierz's Python powered Algorithmic Music Composer\n"
print "To use default settings, press 'enter'\n"
use_file = False
extract = 'x'
if len(sys.argv) > 1:
	use_file = True
	import textpars
	raw = textpars.TextPars(sys.argv[1])
	print "Input data will be read from specified file\n"

else:
	print "Cellular Automata data selected\n"
	done = False
	ca_size = 7 # default
	while done == False:
		print "Enter size of x/y axes\n[Default = 7]:"
		i = raw_input()
		if i != '':
			try:
				i = int(i)
				if i > 2:
					ca_size = i
					done = True
				else:
					print "Size is too small. Enter 3 or greater"
			except ValueError:
				print "Invalid input. Please enter just an integer"
		else:
			done = True
	
	done = False
	while done == False:
		print "Enter number of seeds\n[Default = 3]:"
		seeds = 3
		s = raw_input()
		if s != '':
			try:
				s = int(s)
				if s > (i*i):
					print "More seeds than available cells. Enter a lower number"
				elif s > 0:
					done = True
				else:
					print "Number of seeds must be at least 1"
			except ValueError:
				print "Invalid input. Please enter an integer"
		else:
			done = True
	extract = 'x'
	done = False
	while done == False:
		print "Select extraction method, type 'x' or 'y' to use appropriate axis\n[Default='x']"
		e = raw_input()
		if e == '':
			done = True
		elif e == 'x':
			done = True
		elif e == 'y':
			extract = 'y'
			done = True
		else:
			print "Invalid input. Enter 'x' or 'y'"

	import cell
	global raw
	raw = cell.Cell(ca_size, ca_size, extract)
	raw.seed(seeds)

# OBSOLETE
def get_data():
	return raw.get_data()

# Now we get the time signature to use
sig = '4/4'

print "\nPlease enter time signature as two integers seperated by a forward slash; eg: 2/4, 3/4 or 4/4. Warning large values are not recommended.\nDefault=4/4"
done = False
while done == False:
	s = raw_input()
	if s == '':
		done = True
	else:
		try:
			s.index('/')
			temp = s.split('/')
			int(temp[0])
			int(temp[1])
			sig = s
			done = True

		except ValueError:
			print "Invalid time signature. Format should be 4/4, 3/4 etc"

# Now we get the tempo

tempo = 2

print "\nPlease enter tempo as an integer between 1 and 5\n[Default=2]:"
done = False
while done == False:
	t = raw_input()
	if t == '':
		done = True
	else:
		try:
			t = int(t)
			if 0 < t < 6:
				tempo = t
				done = True
			else:
				print "Invalid tempo. Enter integer between 1 and 5"
		except ValueError:
			print "Invalid tempo. Enter integer between 1 and 5"


# Now we'll get what scale to use

scale = 1

print "\nPlease select which scale to use: \n1) Minor Pentatonic\n2) Blues\n3) Major\n4) In-Sen\n[Default=1]:"

done = False
while done == False:
	s = raw_input()
	if s == '':
		done = True
	else:
		try:
			s = int(s)
			if 0 < s < 5:
				scale = s
				done = True
			else:
				print "Invalid input. Enter 1-4"
		except ValueError:
			print "Invalid input. Enter an integer 1-4"


# Now we get what key to use

key = 'a'
allowed = ['a','a#','b','c','c#','d','d#','e','f','f#','g','g#']

print "\nSelect enter a key to use. eg: a, a#, b, c etc\n[Default=a]"

done = False
while done == False:
	k = raw_input()
	if k == '':
		done = True
	else:
		k = k.lower()
		if k in allowed:
			key = k
			done = True
		else:
			print "Invalid input. Valid inputs:"
			print allowed

del allowed # we dont need this anymore


# Now we get it all moving

import structure
struct = structure.Structure(sig, tempo)

if scale == 1:
	from mpent import *
	map = MPent(key)
elif scale == 2:
	from blues import *
	map = Blues(key)
elif scale == 3:
	from major import *
	map = Major(key)
else:
	from insen import *
	map = InSen(key)


import segman
manager = segman.SegMan()

# Now we'll find out what notes to play

import player
play = player.Player(raw, map, struct, manager)

import output
out = output.Output()

stop = False

# Keeps running until ctrl-c'ed. the code allows this.
while stop == False:
	stop = True
	x = out.run(play.run())
	if x == 1:
		stop = False


