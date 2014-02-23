import Queue
import time

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

		inputNode = [0, self.agentPosition, self.T, "00000"]
		return self.makeSearch(inputNode)[0]

	def makeSearch(self, inputNode):
		j, i = inputNode[1]
		if self.grid[i][j] == "E":
			return inputNode

		visited = [[[[0 for l in xrange(32)] for k in xrange(self.T)] for j in xrange(self.M)] for i in xrange(self.N)]
		visited[i][j][inputNode[2] - 1][int(inputNode[3])] == 1
		node = inputNode
		fringe = Queue.Queue()
		while True:
			next = self.getSuccessors(node)
			for item in next:
				j,i = item[1]
				if self.grid[i][j] == "E":
					return item
				if  visited[i][j][item[2] - 1][int(item[3], 2)] == 0:
					
					fringe.put(item)
					visited[i][j][item[2] - 1][int(item[3], 2)] = 1
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
			if potentialName == "X":
				continue
			elif potentialName == "E":
				return [[node[0] + 1, (j, i), node[2], node[3]]]
			elif potentialName == "O" or potentialName == "S":
				successors.append([node[0] + 1, (j, i), node[2], node[3]])
			elif potentialName == "M":
				if node[2] - 1 != 0:
					successors.append([node[0] + 1, (j, i), node[2] - 1, node[3]])
			
			elif potentialName[0] == "G":
				keys = []
				for char in node[3]:
					keys.append(char)
				if keys[int(self.grid[i][j][1]) - 1] == "1":
					successors.append([node[0] + 1, (j, i), node[2], node[3]])

			elif potentialName[0] == "K":
				keys = []
				for char in node[3]:
					keys.append(char)
				keys[int(potentialName[1]) - 1] = "1"
				successors.append([node[0] + 1, (j, i), node[2], "".join(keys)])

		return successors

newSearch = Search()
print newSearch.solve(input4)