# The minor pentatonic subclass extends mapper

from mapper import *

class MPent(Mapper):
	
	def __init__(self, key):
		Mapper.__init__(self, key)
		self.scale = [0,3,5,7,10,12,15,17,19,22,24,27]
		self.move1 = [-5,-2,-1,0,1,2,5]
		self.move2 = [-4,-3,3,4]
		self.threshold = 75


