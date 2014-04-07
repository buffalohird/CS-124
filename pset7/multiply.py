class Solution:
	def solve(self):

		self.T = int(raw_input())
		self.prime = 795028841
		tests = []

		for i in xrange(self.T):
			tests.append(raw_input().split())

		for i in xrange(self.T):
			self.helper(tests[i])
	
	def helper(self, test):
		N,M,P = test[0], test[1], test[2]

		N = self.helper2(N)
		M = self.helper2(M)
		P = self.helper2(P)

		#print (N * M) % self.prime, int(P) % self.prime
		if (N * M) % self.prime == int(P):
			print "yes"
		else:
			print "no"


	def helper2(self, number):
		numberLength = len(number)
		counter = int(number[0])
		for i in xrange(numberLength - 1):
			counter = counter % self.prime
			counter = counter * 10 + int(number[i+1])



		return counter % self.prime

solution = Solution()
solution.solve()