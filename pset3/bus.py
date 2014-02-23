import Queue

class moneyBus:

	def calcPathCost(self, vertex1, vertex2, pathCost):
		return pathCost - self.P[vertex2]

	def solve(self):
		self.N, self.E = map(int, raw_input().split())
		self.edges = [[float("inf") for _ in xrange(self.N)] for _ in xrange(self.E)]
		self.P = map(int, raw_input().split())
		for item in xrange(self.E):
			i, j, k = map(int, raw_input().split())
			self.edges[i - 1][j - 1] = k

		# initialize graph
		distance = [float("inf") for _ in xrange(self.N)]
		predecessor = [None for _ in xrange(self.N)]
		distance[0] = 0

		for vertex in xrange(self.N):
			for edge in self.edges:
				if distance[edge[0]]


		

		#currentPosition = [0, 1]
		"""
		for vertex in xrange(self.N):
			shortestPaths[vertex][vertex] = 0
			outnodes = self.edges[vertex]
			for item in outnodes:
				if item != float("inf"):
					itemIndex = outnodes.index(item)
					totalWeight = self.calcPathCost(vertex, itemIndex, item)
					shortestPaths[vertex][itemIndex] = totalWeight

		for k in xrange(self.N):
			for i in xrange(self.N):
				for j in xrange(self.N):
					if shortestPaths[i][j] > shortestPaths[i][k] + shortestPaths[k][j]:
						shortestPaths[i][j] = shortestPaths[i][k] + shortestPaths[k][j]

		for item in shortestPaths:
			print item
		"""
			
			
			
		return 0



problem = moneyBus()
print problem.solve()
