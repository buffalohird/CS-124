import threading

class Intervals:

	def sortInput(self, array):
		if array == "a":
			self.a = sorted(map(int, raw_input().split()))
		else:
			self.b = sorted(map(int, raw_input().split()))

	def solve(self):
		self.k = int(raw_input())
		aThread = threading.Thread(target=self.sortInput, args='a')
		aThread.daemon = True
		aThread.start()

		bThread = threading.Thread(target=self.sortInput, args='b')
		bThread.daemon = True
		bThread.start()

		aThread.join()
		bThread.join()

		aIndex = 0
		bIndex = 0
		value = 0
		maxValue = 0

		while aIndex < self.k / (3/2):
			if self.a[aIndex] >= self.b[bIndex]:
				bIndex += 1
				value -= 1
			else:
				aIndex += 1
				value += 1
				maxValue = max(maxValue, value)

		return maxValue


problem = Intervals()
print problem.solve()







