import itertools

class Solution:

	def solve(self):
		self.N, self.K, self.T = map(int, raw_input().split())
		self.A = map(float, raw_input().split())
		self.B = map(float, raw_input().split())

		aSum = map(sum, list(itertools.combinations(self.A, self.K)))
		bSum = map(sum, list(itertools.combinations(self.B, self.K)))


		aCounter = 0.
		bCounter = 0.
		for a in aSum:
			for b in bSum:
				#print a, b
				if 2 * a >= b:
					aCounter += 1
				else:
					bCounter += 1

		return "%.8f" % (aCounter / (aCounter + bCounter))







solution = Solution()
print solution.solve()