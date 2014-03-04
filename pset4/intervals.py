

class Intervals:

	def solve(self):
		self.k = int(raw_input())
		self.a = map(lambda x: [int(x), 1], raw_input().split())
		self.b = map(lambda y: [int(y), -1], raw_input().split())
		values = [0] * self.k * 2
		newList = sorted(self.a + self.b)
		newListLength = len(newList)
		print newList

		for index in xrange(newListLength / 2 + 5):
			values[index] += newList[index][1] + values[index - 1]
		return max(values)

problem = Intervals()
print problem.solve()





