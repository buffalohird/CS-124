from math import log, ceil, floor
import time



class Solution:
	def solve2(self, k, l1, l2, r1, r2):
		#print k, l1, r1, l2, r2
		length1 = r1 - l1
		length2 = r2 - l2

		if length1 == 0 or length2 == 0:
			return 0

		if l1 <= l2 and r1 >= r2:
			return length2

		if l2 <= l1 and r2 >= r1:
			return length1

		kPivot = 2**(k-1) - 1
		overlap = min(r1, r2) - max(l1, l2)
		if overlap >= kPivot:
			return overlap


		if not (l1 <= kPivot <= r1 or l2 <= kPivot <= r2):
			#print l1, l2, r1, r2
			if l1 > kPivot:
				l1 -= kPivot + 1
				r1 -= kPivot + 1
			if l2 >= kPivot:
				l2 -= kPivot + 1
				r2 -= kPivot + 1
			return self.solve2(k - 1, l1, l2, r1, r2)


		"""
		if not (l1 <= kPivot <= r1 and l2 <= kPivot <= r2):
			if l1 > kPivot:
				l1 -= kPivot + 1
				r1 -= kPivot + 1
			if l2 >= kPivot:
				l2 -= kPivot + 1
				r2 -= kPivot + 1
			return self.solve2(k - 1, l1, l2, r1, r2)
		"""

		l1a, r1a, l1b, r1b = 0, 0, 0, 0
		if l1 > kPivot:
			l1 -= kPivot + 1
			r1 -= kPivot + 1
		if l2 > kPivot:
			l2 -= kPivot + 1
			r2 -= kPivot + 1

		if r1 < kPivot:
			l1a = l1
			r1a = r1
			l1b = 0
			r1b = 0
		else:
			l1a = l1
			r1a = kPivot
			l1b = 0
			r1b = r1 - (kPivot + 1)

		if r2 < kPivot:
			l2a = l2
			r2a = r2
			l2b = 0
			r2b = 0
		else:
			l2a = l2
			r2a = kPivot
			l2b = 0
			r2b = r2 - (kPivot + 1)


		return max(overlap, self.solve2(k-1, l1a, l2b, r2a, r2b), self.solve2(k-1, l1b, l2a, r1b, r2a), self.solve2(k-1, l1a, l2a, r2a, r2a), self.solve2(k-1, l1b, l2b, r1b, r2b))

	def solve(self):
		#startTime = datetime.now()
		self.k = int(raw_input())
		self.l1, self.r1, self.l2, self.r2 = map(int, raw_input().split())


		return self.solve2(self.k, self.l1, self.l2, self.r1, self.r2)

		length1 = self.r1 - self.l1
		length2 = self.r2 - self.l2

		if self.l1 <= self.l2 and self.r1 >= self.r2:
			return length2

		if self.l2 <= self.l1 and self.r2 >= self.r1:
			return length1



		k = self.k
		kPivot = 2**(k-1) - 1
		#print kPivot
		while not (self.l1 <= kPivot <= self.r1 and self.l2 <= kPivot <= self.r2):
			print self.l1, self.r1, self.l2, self.r2
			#print k
			#print kPivot
			if self.l1 > kPivot:
				self.l1 -= kPivot + 1
				self.r1 -= kPivot + 1
			if self.l2 >= kPivot:
				self.l2 -= kPivot + 1
				self.r2 -= kPivot + 1
			if self.l1 <= self.l2 and self.r1 >= self.r2:
				return length2

			if self.l2 <= self.l1 and self.r2 >= self.r1:
				return length1

			overlap = min(self.r1, self.r2) - max(self.l1, self.l2)
			if overlap >= kPivot:
				return overlap

			k -= 1
			kPivot = 2**(k-1) - 1
		print self.l1, self.r1, self.l2, self.r2


		start = min(self.l1, self.l2)
		end = max(self.r1, self.r2)

		if self.l1 <= self.l2 and self.r1 >= self.r2:
			return length2

		if self.l2 <= self.l1 and self.r2 >= self.r1:
			return length1

		overlap = min(self.r1, self.r2) - max(self.l1, self.l2)
		if overlap > kPivot:
			return overlap

		"""
		#print start, end

		mainArray = [0 for _ in xrange(end - start)]



		
		for i in xrange(start, end):
			if i % 2 == 0:
				mainArray[i - start] = 1
			else:
				j = 2
				while j < self.k + 1:
					if (i + 1 - 2**(j-1)) % 2**j == 0:
						mainArray[i - start] = j
						break
					j += 1  


		array1 = mainArray[self.l1 - start : self.r1 - start]
		array2 = mainArray[self.l2 - start : self.r2 - start]
		
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
		#endTime = datetime.now()
		#differenceTime = (endTime - startTime).total_seconds()
		#print differenceTime
		return counter
		

	def getValue(self, position):
		power = self.k
		while log(position, 2) != floor(log(position, 2)):
			#print position
			#print power
			#print "\n"
			if position > 2**power:
				position -= 2**power
			else:
				power -= 1
		#print position
		#print int(log(position, 2)) + 1
		return int(log(position, 2)) + 1


	
	def createArray(self,k):
		if k <= 1:
			return [1]
		else:
			return self.createArray(k-1) + [k] + self.createArray(k-1)
	"""









solution = Solution()
print solution.solve()