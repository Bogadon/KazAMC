# The note mapping module

import copy

class Mapper:

	# takes data as list of values
	def __init__(self, key):
		self.notes = ['f','f#','g','g#','a','a#','b','c','c#','d','d#','e']
		self.offset = self.notes.index(key)
		self.last = -1

		self.move1 = []
		self.move2 = []
		self.threshold = 0
		self.scale = []

	# converts a number to a note
	def get_note(self, x):
		x += self.offset
		octave = 0
		while x > 11:
			octave += 1
			x -= 12

		return self.notes[x] + str(octave)

	# maps val to a note in scale. val should be float
        def map_to_scale(self, val):
		val = float(val)
                if self.last == -1:
                        self.last = 0
                        return 0

                move = []
                divider = self.threshold
                if val < self.threshold:
                        move = copy.deepcopy(self.move1)
                else:
                        move = copy.deepcopy(self.move2)
                        val -= self.threshold
                        divider = 100 - self.threshold

                while True:
			if self.last + move[0] < 0:
				move.pop(0)
			else:
				break
		while True:
			if (self.last + move[(len(move) - 1)]) > 11:
                        	move.pop((len(move) - 1))
			else:
				break


		divider = float(divider)
                divider =  (divider / len(move)) + 0.1
                val = val / divider # get a value we can map to move list
		pos =  (self.last + move[int(val)])

                self.last = pos

                return self.scale[pos]

	# ties everything together
	def map(self, val):
		val = self.map_to_scale(val)

		return self.get_note(val)
