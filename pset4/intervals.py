

class Intervals:

	def solve(self):
		self.k = int(raw_input())
		self.a = map(int, raw_input().split())
		self.b = map(int, raw_input().split())

		print self.k
		print "\n"
		for item in self.a:
			print item
		print "\n"
		for item in self.b:
			print item

		intervals = []

		for index in xrange(len(self.a)):
			intervalStart = self.a[index]
			intervalEnd = self.b[index]
			addedBool = False
			if len(intervals) == 0:
				intervals.append([[intervalStart, intervalEnd]])
			for group in intervals:
				overlapBool = False
				for item in group:
					if intervalStart <= item[0]:
						if intervalEnd > item[0]:
							overlapBool = True
							print "[%d, %d]  overlapping prexisting [%d, %d]" % (intervalStart, intervalEnd, item[0], item[1])
					elif intervalStart > item[0]:
						if intervalStart < item[1]:
							overlapBool = True
							print "[%d, %d]  overlapping prexisting [%d, %d]" % (intervalStart, intervalEnd, item[0], item[1])
				if overlapBool == False:
					print "adding", intervalStart, intervalEnd
					addedBool = True
					group.append([intervalStart, intervalEnd])
			if addedBool == False:
				intervals.append([[intervalStart, intervalEnd]])
					#if intervalStart > item[0] and intervalStart < item[1] or intervalEnd > item[0] and intervalEnd < item[1]:
					#print "[%d, %d]  contained in prexisting [%d, %d]" % (intervalStart, intervalEnd, item[0], item[1])
		print intervals


problem = Intervals()
print problem.solve()



