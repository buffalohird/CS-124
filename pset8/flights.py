import itertools
import Queue

def solve():
       
	N, nE, nW, F = map(int, raw_input().split())
	indicesE = map(int, raw_input().split())
	populationsE = map(int, raw_input().split())
	indicesW = map(int, raw_input().split())
	indicesW = sorted(indicesW)
	flights = []
	maxSearchValue = 5
	indicesELength = len(indicesE)
	indicesWLength = len(indicesW)

	for _ in xrange(F):
		flights.append(map(int, raw_input().split()))
	flights = sorted(flights, key = lambda x: (x[0], x[1]))


	indicesE, populationsE = zip(*sorted(zip(indicesE, populationsE)))
	indicesE = list(indicesE)
	populationsE = list(populationsE)

	populationSum = sum(populationsE)

	originalConstraintsGraph = createOriginalGraph(flights, 2, N)
	originalTimesGraph = createOriginalGraph(flights, 3, N)

	maxConstraintsIndex = len(originalConstraintsGraph)
	parent = [0 for _ in xrange(maxConstraintsIndex)]

	def isPath(indicesW, indexE):
		for j in indicesW:
			if bfs(originalConstraintsGraph, indexE, j, parent):
				return True
		return False

	for indexE in indicesE:
		if not isPath(indicesW, indexE):
			return -1

	for T in xrange(0, 1000):
		graph = createNewGraph(originalConstraintsGraph, originalTimesGraph, indicesE, populationsE, indicesW, N, T+1)
		maxIndex = len(graph)

		flow = solveMaxFlow(graph, 0, maxIndex - 1)
		if flow >= populationSum:
			return T

	return -1

"""
def solve2():

	matrix = []
	for _ in xrange(6):
		matrix.append(map(int, raw_input().split()))

	return solveMaxFlow(matrix, 0, 5)
"""

def addSource(graph, indicesE, populationsE, index, N, T):

	counter = 0 
	maxIndex = N*T + 1
	indicesELength = len(indicesE)
	graph[index][0] = 0

	for i in xrange(N): 
		if counter != indicesELength and i == indicesE[counter]: 
			for j in xrange(T): 
				graph[0][1 + i*T + j] = populationsE[counter]
			counter += 1
		else: 
			for j in xrange(T): 
				graph[0][1 + i*T + j] = 0
	graph[index][maxIndex] = 0

	return graph

def addSink(graph, indicesW, N, T): 

	counter = 0 
	maxIndex = N*T + 1
	indicesWLength = len(indicesW)
	maxPopulation = 10000
	graph[0][maxIndex] = 0

	for i in xrange(N):
		if counter != indicesWLength and i == indicesW[counter]: 
			for j in xrange(T): 
			    graph[1 + i*T + j][maxIndex] = maxPopulation
			counter += 1
		else: 
			for j in xrange(T): 
				graph[1 + i*T + j][maxIndex] = 0
	for k in xrange(N*T + 2): 
		graph[maxIndex][k] = 0
	return graph

def createNewGraph(cGraph, tGraph, indicesE, populationsE, indicesW, N, T): 

	graph = []
	maxIndex = N*T + 2

	for i in xrange(maxIndex): 
		tempGraph = []
		for j in xrange(maxIndex): 
			tempGraph.append(0)
		graph.append(tempGraph)

	graph = addSource(graph, indicesE, populationsE, 0, N, T)

	for i in xrange(N): 
		for j in xrange(N): 
			if cGraph[i][j] == 0: 
			    continue
			else: 
			    c, t = cGraph[i][j], tGraph[i][j]
			    iIndexStart, jIndexStart = 1 + i*T, 1+ j*T
			for k in xrange(T - t): 
				graph[iIndexStart + k][jIndexStart + t + k] = c

	graph = addSink(graph, indicesW, N, T)

	return graph

def createOriginalGraph(flights, index, maxIndex): 

	flightLength = len(flights)
	graph = []
	counter = 0
	completionBool = False

	for i in xrange(maxIndex):
		tempGraph = [] 
		for j in xrange(maxIndex): 
			if counter == flightLength: 
				completionBool = True
			else:
				currentFlight = flights[counter]
			if not completionBool and currentFlight[0] == i and currentFlight[1] == j: 
				counter += 1
				tempGraph.append(currentFlight[index])
			else:
				tempGraph.append(0)
		graph.append(tempGraph)
	return graph

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

print solve()