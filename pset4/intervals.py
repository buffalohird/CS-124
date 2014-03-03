

class Intervals:

	def solve(self):
		self.k = int(raw_input())
		self.a = map(int, raw_input().split())
		self.b = map(int, raw_input().split())

		newArray = sorted(zip(self.a,self.b))
		arrayEnd = max(self.b)
		#arrayStart = max(self.a)
		values = [0] * arrayEnd

		for (a,b) in newArray:
			print a, b
			for i in xrange(b - a):
				values[a + i] += 1

		return max(values)



problem = Intervals()
print problem.solve()



