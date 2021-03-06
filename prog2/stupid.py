import Queue
import time

class Search:


	def solve(self, input=""):
		self.grid = []
		
		
		
		self.N, self.M, self.T = map(int, raw_input().split())
		for item in xrange(self.N):
			self.grid.append(map(str, raw_input().split()))
		"""
		self.N, self.M, self.T = map(int, input[0].split())
		for i in xrange(self.N):
			self.grid.append(map(str, input[i+1].split()))
		"""
		
		for item in self.grid:
			for state in item:
				if state == "S":
					self.agentPosition = (item.index(state), self.grid.index(item))

		inputNode = [0, self.agentPosition, self.T, ("K0")]
		return self.makeSearch(inputNode)[0]

	def makeSearch(self, inputNode):
		visited = set()
		visited.add((inputNode[1], inputNode[2], inputNode[3]))
		node = inputNode
		fringe = Queue.Queue()
		while True:
			next = self.getSuccessors(node)
			for item in next:
				j,i = item[1]
				if self.grid[i][j] == "E":
					return item
				if (item[1], item[2], item[3]) not in visited:
					fringe.put(item)

			while node[2] > 0:
				visited.add((node[1], node[2], node[3]))
				node[2] -= 1
			if fringe.empty():
				return [-1, None, None, None]
			else:
				node = fringe.get()


	def getSuccessors(self, node):
		#currentKeys = node[3]
		x,y = node[1]
		potentials = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
		successors = []
		for (j, i) in potentials:
			if j > self.M - 1 or i > self.N -1 or j < 0 or i < 0:
				continue
			if self.grid[i][j] == "E":
				return [[node[0] + 1, (j, i), node[2], node[3]]]
			if self.grid[i][j] == "O" or self.grid[i][j] == "S":
				successors.append([node[0] + 1, (j, i), node[2], node[3]])
			if self.grid[i][j] == "M":
				if node[2] - 1 != 0:
					successors.append([node[0] + 1, (j, i), node[2] - 1, node[3]])
			"""
			if self.grid[i][j][0] == "G":
				for key in node[3]:
					if self.grid[i][j][1] == key[0][1]:
						successors.append([node[0] + 1, (j, i), node[2], node[3]])
			if self.grid[i][j][0] == "K":
				foundKeyBool = False
				for key in node[3]:
					if self.grid[i][j][1] == key[0][1]:
						successors.append([node[0] + 1, (j, i), node[2], node[3]])
						foundKeyBool = True
				if foundKeyBool == False:
					currentKeys.append([self.grid[i][j], (j, i)])
					successors.append([node[0], (j, i), node[2], currentKeys])
			"""


		"""
		print "###state %s, %s has succesors:" % (str(x), str(y))
		for item in successors:
			print item
		print "\n"
		"""

		return successors

input1 = ["4 4 1", "X O O E", "O O X O", "O X X O", "S O O X"]
input2 = ["5 4 3", "M O O E", "O X X M", "O X X M", "O X X M", "M O O S"]
input3 = ["4 4 2", "O O O E", "M X O M", "M X O M", "O O O S"]
input4 = ["4 4 2", "O K2 G2 E", "O O X G1", "O S O O", "O O X K1"]
input5 = ["4 4 1", "X O O E", "X X X X", "O O O O", "S O O O"]
newSearch = Search()
print newSearch.solve(input4)
