# The Cellular Automata Module

import random
class Cell:


	# Creates a grid of cells x by y large and sets each value to 0
	def __init__(self, x, y, method):
		self.x = x
		self.y = y
		self.method = method
		self.grid = {}
		self.MAX = 200
		self.SUBMAX = 100

		a = 0
		b = 0
		while a <= self.x:
			while b <= self.y:
				self.grid[(a,b)] = 0
				b += 1
			a += 1
			b = 0


	# Adds n seeds to grid
	def seed(self, n):
		a = 0
		while a < n:
			val = random.randint(1, self.SUBMAX) #val must be > 0
			xco = random.randint(0, self.x)
			yco = random.randint(0, self.y)
			
			self.grid[(xco, yco)] = val
			a = a + 1
	
	
	# increases time by 1
	def run(self):
		incs = [] # we need to use a list to hold increments so they dont effect current time cycle
		for a,b in self.grid.iteritems():
			if a[0] - 1 >= 0:
				b += self.grid[((a[0] - 1), a[1])]
			if a[0] + 1 <= self.x:
				b += self.grid[((a[0] + 1), a[1])]
			if a[1] - 1 >= 0:
				b += self.grid[(a[0], (a[1] -1))]
			if a[1] + 1 <= self.y:
				b += self.grid[(a[0], (a[1] + 1))]

			# modify values to stop things getting out of hand
			if b > self.MAX:
				b = 0

			if b > self.SUBMAX:
				b -= self.SUBMAX

			incs.append((a, b))

		# Now we change the values to their next time step
		for inc in incs:
			self.grid[inc[0]] = inc[1]
	
	# extracts data along x axis. returns a list of values
	def extract_x(self):
		xco = 0
		yco = 0
		ret = []
		while xco <= self.x:
			while yco <= self.y:
				val = self.grid[(xco, yco)]
				if val != 0:
					ret.append(val)
				yco += 1
			xco += 1
			yco = 0

		self.run() # After extracting run to increase time so theres fresh data for next time
		return ret

	# extracts data along y axis. as above
	def extract_y(self):
		xco = 0
		yco = 0
		ret = []
		while yco <= self.y:
			while xco <= self.x:
				val = self.grid[(xco, yco)]
				if val != 0:
					ret.append(val)
				xco += 1
			yco += 1
			xco = 0

		self.run()
		return ret

	
	# One method to tie everything together
	def get_data(self):
		if self.method == 'x':
			return self.extract_x()
		else:
			return self.extract_y()
