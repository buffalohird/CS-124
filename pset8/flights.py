import itertools

class Solution:

	def solve(self):
		N, nE, nW, F = map(int, raw_input().split())
		indicesE = map(int, raw_input().split())
		populationsE = map(int, raw_input().split())
		indicesW = map(int, raw_input().split())
		populationsE = map(int, raw_input().split())
		flights = []

		for _ in xrange(F - 1):
			flights.append(map(int, raw_input().split()))


		print flights

		
solution = Solution()
print solution.solve()