# The in-sen subclass extends mapper

from mapper import *

class InSen(Mapper):
	
	def __init__(self, key):
		Mapper.__init__(self, key)
		self.scale = [0,1,5,7,10,12,13,17,19,22,24,25]
		self.move1 = [-3,0,3]
		self.move2 = [-4,-2,-1,1,2,4]
		self.threshold = 50


