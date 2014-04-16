import itertools
import Queue


def solve():

	N, nE, nW, F = map(int, raw_input().split())
	indicesE = map(int, raw_input().split())
	populationsE = map(int, raw_input().split())
	indicesW = map(int, raw_input().split())
	populationsE = map(int, raw_input().split())
	flights = []

	for _ in xrange(F - 1):
		flights.append(map(int, raw_input().split()))


	return flights

def solve2():

	matrix = []
	for _ in xrange(6):
		matrix.append(map(int, raw_input().split()))

	print solveMaxFlow(matrix, 0, 5)



def solveMaxFlow(graphMatrix, graphSource, graphSink):
	maxIndex = len(graphMatrix)
	residualsMatrix = [[0 for _ in xrange(maxIndex)] for _ in xrange(maxIndex)]
	for u in xrange(maxIndex):
		for v in xrange(maxIndex):
			residualsMatrix[u][v] = graphMatrix[u][v]

	parent = [0 for _ in xrange(maxIndex)]

	maxFlow = 0

	while (bfs(residualsMatrix, graphSource, graphSink, parent)):
		pathFlow = float("inf")

		v = graphSink
		while v != graphSource:
			u = parent[v]
			pathFlow = min(pathFlow, residualsMatrix[u][v])
			v = parent[v]

		v = graphSink
		while v != graphSource:
			u = parent[v]
			residualsMatrix[u][v] -= pathFlow
			residualsMatrix[v][u] += pathFlow
			v = parent[v]

		maxFlow += pathFlow

	return maxFlow

def bfs(residualsMatrix, source, sink, parent):
	maxIndex = len(residualsMatrix)
	visited = [False for _ in xrange(maxIndex)]

	fringe = Queue.Queue()
	fringe.put(source)
	visited[source] = True
	parent[source] = -1

	while fringe.empty() != True:
		u = fringe.get()

		for v in xrange(maxIndex):
			if visited[v] == False and residualsMatrix[u][v] > 0:
				fringe.put(v)
				parent[v] = u
				visited[v] = True



	return visited[sink] == True







print solve2()