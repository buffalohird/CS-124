import itertools

class Solution:

	def solve(self):
		self.N, self.K, self.T = map(int, raw_input().split())
		self.A = sorted(map(int, raw_input().split()), reverse=False)
		self.B = sorted(map(int, raw_input().split()), reverse=False)

		#print self.A
		#print self.B

		maxSum = self.K*self.T

		self.dp = [[[-1 for _ in xrange(maxSum + 1)] for _ in xrange(self.K + 1)] for _ in xrange(self.N + 1)]
		self.dpB = [[[-1 for _ in xrange(maxSum + 1)] for _ in xrange(self.K + 1)] for _ in xrange(self.N + 1)]


		sumA = [-1 for _ in xrange(maxSum + 1)]
		for i in xrange(maxSum + 1):
			#print i
			sumA[i] = self.recurrence(self.N, self.K, i)

		sumB = [-1 for _ in xrange(maxSum + 1)]
		for i in xrange(maxSum + 1):
			#print i
			sumB[i] = self.recurrenceB(self.N, self.K, i)



		winningSum = 0
		for i in xrange(len(sumA)):
			for j in xrange(len(sumB)):
				if i * 2 >= j:
					winningSum += sumA[i] * sumB[j]

		return "%.8f" % (float(winningSum) / float(sum(sumA))**2)


		for i in xrange(self.N):
			for j in xrange(self.K):
				print i,j, self.dp[i][j]

		print sumA
		print sumB

	def recurrence(self, n, k, value):

		if n == 0:
			if value == 0 and k == 0: return 1
			else: return 0
		if value < 0 or k < 0:
			return 0


		if self.dp[n][k][value] != -1:
			#print n,k,value, self.dp[n][k][value]
			return self.dp[n][k][value]

		returnValue = self.recurrence(n-1,k-1,value - self.A[n - 1]) + self.recurrence(n-1, k, value)
		self.dp[n][k][value] = returnValue
		return returnValue

	def recurrenceB(self, n, k, value):

		if n == 0:
			if value == 0 and k == 0: return 1
			else: return 0
		if value < 0 or k < 0:
			return 0

		if self.dpB[n][k][value] != -1:
			return self.dpB[n][k][value]

		returnValue = self.recurrenceB(n-1,k-1,value - self.B[n - 1]) + self.recurrenceB(n-1, k, value)
		self.dpB[n][k][value] = returnValue
		return returnValue






solution = Solution()
print solution.solve()