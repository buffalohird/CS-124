import Queue
import time
import copy

class Search:


	def solve(self, input=""):
		self.grid = []
		
		
		self.N, self.M, self.T = map(int, raw_input().split())
		startFoundBool = False
		for item in xrange(self.N):
			inputRow = map(str, raw_input().split())
			self.grid.append(inputRow)
			if not startFoundBool and 'S' in inputRow:
				startFoundBool = True
				self.agentPosition = (inputRow.index('S'), item)
		"""
		self.N, self.M, self.T = map(int, input[0].split())
		for i in xrange(self.N):
			self.grid.append(map(str, input[i+1].split()))
		"""
		
		
	

		inputNode = [0, self.agentPosition, self.T, ["K6"]]
		return self.makeSearch(inputNode)[0]

	def makeSearch(self, inputNode):
		visited = [[inputNode[1], inputNode[2], inputNode[3]]]
		visitedDict = {}
		if inputNode[1] not in visitedDict:
			visitedDict[inputNode[1]] = {}
		visitedDict[inputNode[1]][inputNode[2]] = inputNode[3]
		print visitedDict
		node = inputNode
		fringe = Queue.Queue()
		while True:
			#print node
			next = self.getSuccessors(node)
			for item in next:
				j,i = item[1]
				#print item
				if self.grid[i][j] == "E":
					return item
				if [item[1], item[2], item[3]] not in visited:
					fringe.put(item)
			#print "\n"

			while node[2] > 0:
				visited.append([node[1], node[2], node[3]])
				node[2] -= 1
			if fringe.empty():
				return [-1, None, None, None]
			else:
				node = fringe.get()


	def getSuccessors(self, node):
		x,y = node[1]
		potentials = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
		successors = []
		for (j, i) in potentials:
			if j > self.M - 1 or i > self.N -1 or j < 0 or i < 0:
				continue
			potentialName = self.grid[i][j]
			if potentialName == "E":
				return [[node[0] + 1, (j, i), node[2], node[3]]]
			if potentialName == "O" or potentialName == "S":
				successors.append([node[0] + 1, (j, i), node[2], node[3]])
			if potentialName == "M":
				if node[2] - 1 != 0:
					successors.append([node[0] + 1, (j, i), node[2] - 1, node[3]])

			if potentialName[0] == "G":
				for key in node[3]:
					#print key
					if self.grid[i][j][1] == key[1]:
						successors.append([node[0] + 1, (j, i), node[2], node[3]])

			if potentialName[0] == "K":
				#print "found a key"
				foundKeyBool = False
				for key in node[3]:
					#print key

					if potentialName[1] == key[1]:
						successors.append([node[0] + 1, (j, i), node[2], node[3]])
						continue
						#foundKeyBool = True
				if foundKeyBool == False:
					successors.append([node[0] + 1, (j, i), node[2], node[3] + [potentialName]])

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
input4 = ["4 4 2", "O K1 G2 E", "M M X G1", "O S O O", "O O X K2"]
input5 = ["4 4 1", "X O O E", "X X X X", "O O O O", "S O O O"]
newSearch = Search()
print newSearch.solve(input4)

