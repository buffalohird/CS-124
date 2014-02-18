
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
		keys = []
		gates = []
		for item in self.grid:
			for state in item:
				if state == "S":
					self.agentPosition = (item.index(state), self.grid.index(item))
				if state == "E":
					self.goalPosition = (item.index(state), self.grid.index(item))
				if state[0] == "K":
					keys.append([str(state[1]), (item.index(state), self.grid.index(item))])
				if state[0] == "G":
					gates.append([str(state[1]), (item.index(state), self.grid.index(item))])

		keys.sort(key=lambda item: item[0])
		gates.sort(key=lambda item: item[0])


		states = [j for i in zip(keys, gates) for j in i]
		for item in states:
			self.goalStates.append(item[1])
		self.goalStates.append(self.goalPosition)


		inputNode = [self.agentPosition, 0, self.T]
		for goal in self.goalStates:
			inputNode = self.makeSearch(inputNode, goal)
			j, i = goal
			self.grid[i][j] = "O"
			"""
			print "\n"
			print "returned node from iteration"
			print inputNode
			print "\n"
			"""


			#for item in self.grid:
				#print item


		return inputNode[1]



		#print self.agentPosition

	def makeSearch(self, inputNode, goal):
		visited = []
		node = inputNode
		fringe = Queue.PriorityQueue()
		while not node[0] == goal:
			next = self.getSuccessors(node[0], goal)

			for item in next:
				newT = node[2] + item[1]
				if newT > 0:
					fringe.put([item[0], node[1] + 1, newT])
				#else:
					#visited.append(item[0])
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

	def getSuccessors(self, position, goal):
		if position == None:
			return []
		x,y = position
		potentials = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
		successors = []
		for (j, i) in potentials:
			if j > self.M - 1 or i > self.N -1 or j < 0 or i < 0:
				continue
			if self.grid[i][j] == "O" or self.grid[i][j] == "E" or self.grid[i][j] == "S" or (j, i) == goal:
				successors.append([(j, i), 0])
			if self.grid[i][j] == "M":
				successors.append([(j, i), -1])

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
input4 = ["4 4 2", "O K1 G2 E", "O O X G1", "O S O O", "O O X K2"]
input5 = ["4 4 1", "X O O E", "X X X X", "O O O O", "S O O O"]
newSearch = Search()
print newSearch.solve(input2)


