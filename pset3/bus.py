import Queue

class moneyBus:

	def calcPathCost(self, edge):
		return edge[2] - self.P[edge[1]]

	def solve(self):
		self.N, self.E = map(int, raw_input().split())
		self.edges = []
		self.P = map(int, raw_input().split())
		for item in xrange(self.E):
			i, j, k = map(int, raw_input().split())
			self.edges.append([i - 1, j - 1, k])

		# initialize graph
		distance = [float("inf") for _ in xrange(self.N)]
		predecessor = [None for _ in xrange(self.N)]
		distance[0] = 0 - self.P[0]

		for vertex in xrange(self.N):
			for edge in self.edges:
				newPathCost = distance[edge[0]] + self.calcPathCost(edge)
				if newPathCost < distance[edge[1]]:
					distance[edge[1]] = newPathCost
					predecessor[edge[1]] = edge[0]

		if distance[self.N - 1] == float("inf"):
			return "none"

		for edge in self.edges:
			if distance[edge[0]] + self.calcPathCost(edge) < distance[edge[1]]:
				return "infinity"

		return -1 * distance[self.N - 1]


problem = moneyBus()
print problem.solve()
