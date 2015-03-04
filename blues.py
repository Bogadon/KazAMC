# The Blues subclass extends mapper

from mapper import *

class Blues(Mapper):
	
	def __init__(self, key):
		Mapper.__init__(self, key)
		self.scale = [0,3,4,5,7,10,12,15,17,18,19,22,24,27]
		self.move1 = [-3,-2,-1,0,1,2,3]
		self.move2 = [-6,-5,-4,4,5,6]
		self.threshold = 75


