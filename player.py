# The Player module, ties together what to play next

import time

class Player:

	def __init__(self,rawobj, mapobj, strucobj, segmanobj):
		self.raw = rawobj
		self.map = mapobj
		self.struct = strucobj
		self.manager = segmanobj

		self.buffer = self.raw.get_data()
		self.firstrun = True
		self.current = []
		self.next = ''
		self.bar = []
	
	def get_next_note(self):
		if len(self.buffer) > 0:
			x = self.buffer.pop(0)
			return self.map.map(x)
		else:
			self.buffer = self.raw.get_data()
			x = self.buffer.pop(0)
			return self.map.map(x)


	def convert_struc(self, halfbar):
		l = len(halfbar)
		n = 0
		while n < l:
			ll = len(halfbar[n])
			nn = 0
			while nn < ll:
				if halfbar[n][nn] == 'new':
					halfbar[n][nn] = self.get_next_note()
				nn += 1
			n += 1

		return halfbar


	def new_bar(self):
		struc1 = self.convert_struc(self.struct.create_new(1))
		struc2 = self.convert_struc(self.struct.create_new(2))
		return [struc1, struc2]

	def sim_bar(self):
		struc1 = self.convert_struc(self.struct.create_similar(self.current[0]))
		struc2 = self.convert_struc(self.struct.create_similar(self.current[1]))
		return [struc1, struc2]

	# gets a bar of same structure
	def same_bar(self):
		struc1 = self.convert_struc(self.struct.clean(self.current[0]))
		struc2 = self.convert_struc(self.struct.clean(self.current[1]))
		return [struc1, struc2]

	# Heres where we run it

	def run(self):
		print self.next
		if self.firstrun == True:
			self.current = self.new_bar()
			self.next, self.bar = self.manager.run(self.current)
			self.firstrun = False

		else:
			if self.next == "new_new":
				self.current = self.new_bar()
				self.next, self.bar = self.manager.run(self.current)
		
			elif self.next == "new_sim":
				self.current = self.sim_bar()
				self.next, self.bar = self.manager.run(self.current)

			elif self.next == "new_same":
				self.current = self.same_bar()
				self.next, self.bar = self.manager.run(self.current)

			else:
				self.current = self.bar
				self.next, self.bar = self.manager.run(self.current)

		
		return self.current
