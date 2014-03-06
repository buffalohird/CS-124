class Solution:
	def solve(self):
		self.k = int(raw_input())
		self.l1, self.r1, self.l2, self.r2 = map(int, raw_input().split())


		mainArray = self.createArray(self.k)
		#print mainArray

		array1 = mainArray[self.l1 : self.r1]
		array2 = mainArray[self.l2 : self.r2]
		length1 = len(array1)
		length2 = len(array2)
		maxCounter = 0

		#start = min(self.l1, self.l2)
		#end = max(self.r1, self.r2)

		#arraySolve = mainArray[start : end]
		#print array1
		#print array2


		for i in xrange(length1):
			#print "\n"
			#print "array1 item: " + str(i)
			for j in xrange(length2):
				#print "array2 item: " + str(j)
				k = 0
				while i + k < length1 - 1 and j + k < length2 - 1 and array1[i + k] == array2[j + k]:
					#print array1[i + k]
					#print array2[j + k]
					k += 1
					maxCounter = max(k, maxCounter)


		return maxCounter

	def createArray(self,k):
		if k == 1:
			return [1]
		else:
			return self.createArray(k-1) + [k] + self.createArray(k-1)








solution = Solution()
print solution.solve()