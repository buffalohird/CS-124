

class Intervals:

	def solve(self):
		self.k = int(raw_input())
		self.a = map(lambda x: [int(x), 1], raw_input().split())
		self.b = map(lambda y: [int(y), -1], raw_input().split())

		arrayEnd = max(self.b)[0]
		values = [0] * arrayEnd * 2

		newList = radixsort(self.a + self.b)
		newListLength = len(newList)
		for index in xrange(newListLength):
			values[index] += newList[index][1] + values[index - 1]

		return max(values)



problem = Intervals()
print problem.solve()





