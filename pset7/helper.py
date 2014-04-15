# run through string number and do that mod shit



def helper2(self, number):
		numberLength = len(number)
		counter = int(number[0])
		for i in xrange(len(number) - 1):
			counter = counter % 13
			counter += counter * 10 + int(number[i+1])

		return counter
