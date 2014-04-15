import operator


class Solution:

	def solve(self):
		self.K = int(raw_input())
		self.intervals = []
		self.dp = [-1 for _ in xrange(self.K + 1)]

		for _ in xrange(4):
			self.intervals.append(map(int, raw_input().split()))

		# sort these fuckers
		self.intervals = zip(*self.intervals)
		
		self.intervals = sorted(self.intervals, key=lambda x: x[3])

		return self.recursive(self.K - 1)

	def recursive(self, i):
		if i == 0:
			return 1
		if self.dp[i] != -1:
			return self.dp[i]
		else:
			result = max(self.recursive(i-1), self.search(i) + 1)
			self.dp[i] = result
			return result

	def search(self, i):
		for j in xrange(i - 1, 0, -1):
			print i, j
			print self.intervals[j][3], self.intervals[i][0]
			if self.intervals[j][3] <= self.intervals[i][0]:
				print i, j, self.recursive(j)
				return self.recursive(j)

		return 0

solution = Solution()
print solution.solve()
