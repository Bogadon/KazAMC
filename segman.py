# The Segment Manager module. aka 'the Overlord'

import random

class SegMan:

	def __init__(self):
		self.sequence = []

	# takes a bar of notes/actions and decides what to do next
	def run(self, bar):
		self.sequence.append(bar)
		x = random.randint(0,100)
		if x < 25:
			return ("new_new", [])
		if x < 50:
			return ("new_sim", [])
		if x < 75:
			return ("new_same", [])
		if x < 80:
			return ("rep1", self.sequence[(len(self.sequence) - 1)])
		if x < 84:
			if len(self.sequence) < 2:
				return ("new_new", [])
			return  ("rep2", self.sequence[(len(self.sequence) -2)])
		if x < 87:
			if len(self.sequence) < 3:
				return ("new_new", [])
			return ("rep3", self.sequence[(len(self.sequence) -3)])
		if x < 90:
			if len(self.sequence) < 4:
				return ("new_new", [])
			return ("rep4", self.sequence[(len(self.sequence) -4)])
		return ("orig", self.sequence[0])
