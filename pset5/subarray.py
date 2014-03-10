class Solution:
	def solve(self):
		self.k = int(raw_input())
		self.l1, self.r1, self.l2, self.r2 = map(int, raw_input().split())


		mainArray = self.createArray(self.k)

		array1 = mainArray[self.l1 : self.r1]
		array2 = mainArray[self.l2 : self.r2]
		length1 = len(array1)
		length2 = len(array2)
		#print length2
		suffixes = [[0 for _ in xrange(length2 + 1)] for _ in xrange(length1 + 1)]
		counter = 0

		for i in xrange(length1 + 1):
			for j in xrange(length2 + 1):
				if i == 0 or j == 0:
					suffixes[i][j] = 0
				elif array1[i-1] == array2[j-1]:
					suffixes[i][j] = suffixes[i-1][j-1] + 1
					counter = max(counter, suffixes[i][j])
				else:
					suffixes[i][j] = 0

		#for item in suffixes:
		#	print item
		return counter

		
	def createArray(self,k):
		if k <= 1:
			return [1]
		else:
			return self.createArray(k-1) + [k] + self.createArray(k-1)








solution = Solution()
print solution.solve()