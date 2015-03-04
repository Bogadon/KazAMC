# Structuring module
# 'repeat' is never used
import random
class Structure:

	def __init__(self, sig, tempo):
		s = sig.partition('/')
		self.sig1 = int(s[0])
		self.sig2 = int(s[2])

		self.tempo = tempo

	# generates what to do at a particular moment
	def gen_state(self):
		x = random.randint(0, 100)
		if x < 20:
			return 'pause'
		if x < 60:
			return 'new'
		if x < 80:
			return 'repeat'
		
		return 'extend'

	# creates a new half bar
	def create_new(self, step):
		if step == 1:
			sig = self.sig1
		else:
			sig = self.sig2

		ret = []
		a = 1
		while a <= sig:
			b = 1
			beat = []
			while b <= self.tempo:
				beat.append(self.gen_state())
				b += 1
			ret.append(beat)
			a += 1
	
		ret[0][0] = 'new' #make sure the first note played is always new..
		return ret

	def clean(self, halfbar):
		allowed = ['pause', 'new', 'repeat', 'extend']
		for n in range(0, len(halfbar)):
			for m in range(0, len(halfbar[n])):
				if halfbar[n][m] not in allowed:
					halfbar[n][m] = 'new'

		return halfbar



	# takes a previous half bar and changes 1 beat
	def create_similar(self, halfbar):
		
		halfbar = self.clean(halfbar)
		x = random.randint(0, (len(halfbar)-1))
		n = 0
		while n < len(halfbar[x]):
			halfbar[x][n] = self.gen_state()
			n += 1
		
		halfbar[0][0] = 'new' #again make sure it starts with a new
		return halfbar
