
class Intervals:
	def solve(self):
		self.k = int(raw_input())
		self.a = sorted(map(int, raw_input().split()))
		self.b = sorted(map(int, raw_input().split()))
		aIndex = 0
		bIndex = 0
		value = 0
		maxValue = 0

		while aIndex < self.k:
			if self.a[aIndex] >= self.b[bIndex]:
				bIndex += 1
				value -= 1
			else:
				aIndex += 1
				value += 1
				if value > maxValue:
					maxValue = value
		return maxValue
problem = Intervals()
print problem.solve()




