

class Intervals:

	def solve(self):
		self.k = int(raw_input())
		self.a = map(int, raw_input().split())
		self.b = map(int, raw_input().split())

		newArray = sorted(zip(self.a,self.b))
		maxCounter = 0
		counter = 0
		aCounter = 0
		bCounter = 0
		while True:
			a = newArray[aCounter][0]
			b = newArray[bCounter][1]
			previousB = newArray[bCounter - 1][1]
			#print a, b, counter
			if a < b:
				counter += 1
				aCounter += 1
			else:
				maxCounter = max(maxCounter, counter)
				aCounter -= counter
				counter = 0
				bCounter += 1

			if aCounter >= self.k or bCounter >= self.k:
				return maxCounter




problem = Intervals()
print problem.solve()



