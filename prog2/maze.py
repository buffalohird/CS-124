__author__ = 'thegator12321'

import Queue
#import time

class Search:


	def solve(self, input=""):
		self.grid = []



		"""self.N, self.M, self.T = map(int, raw_input().split())

		for item in xrange(self.N):
			self.grid.append(map(str, raw_input().split()))"""

		self.N, self.M, self.T = map(int, input[0].split())
		for i in xrange(self.N):
			self.grid.append(map(str, input[i+1].split()))

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

		for key in keys:
			self.goalStates.append(key[1])

		#states = [j for i in zip(keys, gates) for j in i]
		#for item in states:
			#self.goalStates.append(item[1])
		self.goalStates.append(self.goalPosition)

		inputNode = [0, self.agentPosition, self.T, []]
		for goal in self.goalStates:
			inputNode = self.makeSearch(inputNode, goal)
			j, i = goal

			"""
			print "\n"
			print "returned node from iteration"
			print inputNode
			print "\n"
			"""


		return inputNode[0]

	def makeSearch(self, inputNode, goal):
		visited = []
		node = inputNode
		fringe = Queue.Queue()

		# put first node on the queue
		# while (the queue isn't empty)
		# take something form the queue
		# get successors
		# is one of them final?
		# are these visited? if not add to queue


		while not node[1] == goal:
			next = self.getSuccessors(node, goal)
			for item in next:
				fringe.put(item)
			newBool = False
			while not newBool:
				if fringe.empty():
					return [-1, None, None, None]
				item = fringe.get()
				if item[1] not in visited:
					newBool = True
			node = item
			visited.append(item[1])

		return node

	def getSuccessors(self, node, goal):
		currentKeys = node[3]
		if node[1] == None:
			return []
		x,y = node[1]
		potentials = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
		successors = []
		for (j, i) in potentials:
			if j > self.M - 1 or i > self.N -1 or j < 0 or i < 0:
				continue
			print "for (%s, %s) looking at successor (%s, %s)" % (x, y, j, i)
			if self.grid[i][j] == "O" or self.grid[i][j] == "E" or self.grid[i][j] == "S" or (j, i) == goal:
				successors.append([node[0] + 1, (j, i), node[2], node[3]])
			if self.grid[i][j] == "M":
				print "hit a monster have lives:", node[2]
				print "at location ", x, y
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

input1 = ["5 5 2", "S M O M O", "O X O O O", "O X O X O", "O O O X M", "X O M M E"]
input2 = ["5 4 3", "M O O E", "O X X M", "O X X M", "O X X M", "M O O S"]
input3 = ["4 4 2", "O O O E", "M X O M", "M X O M", "O O O S"]
input4 = ["4 4 2", "O K2 G2 E", "O O X G1", "O S O O", "O O X K1"]
input5 = ["4 4 1", "X O O E", "X X X X", "O O O O", "S O O O"]
newSearch = Search()




print newSearch.solve(input1)
