# A text parsing module to convert text to numeric data

class TextPars:

	def __init__(self, file):
		self.file = open(file, 'r')

	
	# Converts a character to a numeric value
	def convert(self, c):
		nums = range(0,10)
		ret = 0
		if c in nums:
			ret = 1
		elif c == " ":
			ret = 2
		elif c == ",":
			ret = 3
		elif c == ".":
			ret = 4
		elif c == ";":
			ret = 5
		elif c == ":":
			ret = 6
		elif c == "'":
			ret = 7
		elif c == '"':
			ret = 8
		elif c == "(":
			ret = 9
		elif c == ")":
			ret = 9
		elif c == "a":
			ret = 12.5
		elif c == "b":
			ret = 16
		elif c == "c":
			ret = 19.5
		elif c == "d":
			ret = 23
		elif c == "e":
			ret = 26.5
		elif c == "f":
			ret = 30
		elif c == "g":
			ret = 33.5
		elif c == "h":
			ret = 37
		elif c == "i":
			ret = 40.5
		elif c == "j":
			ret = 44
		elif c == "k":
			ret = 47.5
		elif c == "l":
			ret = 51
		elif c == "m":
			ret = 54.5
		elif c == "n":
			ret = 58
		elif c == "o":
			ret = 61.5
		elif c == "p":
			ret = 65
		elif c == "q":
			ret = 68.5
		elif c == "r":
			ret = 72
		elif c == "s":
			ret = 75.5
		elif c == "t":
			ret = 79
		elif c == "u":
			ret = 82.5
		elif c == "v":
			ret = 86
		elif c == "w":
			ret = 89.5
		elif c == "x":
			ret = 93
		elif c == "y":
			ret = 96.5
		elif c == "z":
			ret = 100

		
		return ret

	def get_data(self):
		ret = []
		line = self.file.readline()
		line = line.lower()
		line = line.strip()

		end = len(line)
		a = 0

		while a < end:
			val = self.convert(line[a])
			ret.append(val)
			a += 1

		return ret

