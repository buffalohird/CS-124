
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
		
		
		self.goalStates = []
		for item in self.grid:
			for state in item:
				if state == "S":
					self.agentPosition = (item.index(state), self.grid.index(item))
				if state == "E":
					self.goalPosition = (item.index(state), self.grid.index(item))
				if state == "K1":
					self.goalStates.append((item.index(state), self.grid.index(item)))

		self.goalStates.append(self.goalPosition)

		inputNode = [self.agentPosition, 0, self.T]
		for item in self.goalStates:
			inputNode = self.makeSearch(inputNode)

		return inputNode[1]



		#print self.agentPosition

		return self.makeSearch()

	def makeSearch(self, inputNode):
		visited = []
		node = inputNode
		fringe = Queue.PriorityQueue()
		while not node[0] == self.goalPosition:
			next = self.getSuccessors(node[0])

			for item in next:
				newT = node[2] + item[1]
				if newT > 0:
					fringe.put([item[0], node[1] + 1, newT])
				else:
					visited.append(item[0])
			newBool = False
			while not newBool:
				if fringe.empty():
					return [None, -1, None]
				item = fringe.get()
				if item[0] not in visited:
					newBool = True
			node = item
			visited.append(item[0])

		return node

	def getSuccessors(self, position):
		x,y = position
		potentials = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
		successors = []
		for (j, i) in potentials:
			if j > self.M - 1 or i > self.N -1 or j < 0 or i < 0:
				continue
			if self.grid[i][j] == "O" or self.grid[i][j] == "E":
				successors.append([(j, i), 0])
			if self.grid[i][j] == "M":
				successors.append([(j, i), -1])

		#print "###state %s, %s has succesors:" % (str(x), str(y))
		#for item in successors:
			#print item
		#print "\n"
		return successors









input = ["4 4 1", "X O O E", "O O X O", "O X X O", "S O O X"]
input2 = ["5 4 3", "M O O E", "O X X M", "O X X M", "O X X M", "M O O S"]
newSearch = Search()
print newSearch.solve(input2)


