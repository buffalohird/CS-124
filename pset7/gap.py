import operator


class Solution:

	def solve(self):
		self.K = int(raw_input())
		intervals = []



		for _ in xrange(4):
			intervals.append(map(int, raw_input().split()))


		# sort these fuckers
		intervals = zip(*intervals)
		

		intervals = sorted(intervals, key=lambda x: x[3])

		
		index = 1
		intervalsLength = len(intervals)
		newIntervals = []
		print intervals
		item = [intervals[0][0], intervals[0][3], 1]
		while index < intervalsLength:
			print item
			if intervals[index][0] >= item[1]:
				print "hello"
				item[2] += 1
				item[1] = intervals[index][3]
				index += 1
			else:
				print "bye"
				index += 1
				if index < intervalsLength:
					newIntervals.append(item)
					item = [intervals[index][0], intervals[index][3], 1]


		newIntervals.append(item)

		print newIntervals




			

	


		# merge intervals and do weights instead


		#dp that shit


		return 6






solution = Solution()
print solution.solve()
