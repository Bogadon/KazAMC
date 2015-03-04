# The Major subclass extends mapper

from mapper import *

class Major(Mapper):
	
	def __init__(self, key):
		Mapper.__init__(self, key)
		self.scale = [0,2,4,5,7,9,11,12,14,16,17,19,21,23,24,26]
		self.move1 = [-4,-2,0,2,4]
		self.move2 = [-7,-6,-5,-3,-1,1,3,5,6,7]
		self.threshold = 65


