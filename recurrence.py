from datetime import datetime

def solve_recurrences(line_1, line_2, line_3):


	K, N = map(int, line_1.split())
	a = map(int, line_2.split())
	c = map(int, line_3.split())
	i = len(a) - 1

	return solve_helper(K, N, a, c, i)

	
	
def solve_helper(K, N, a, c, i):
	if i == N:
		return a.pop() % 1000

	new_result_list = zip(reversed(a), c)
	new_result = reduce(lambda sum, (x, y): sum + x*y, new_result_list, 0)
	a.append(new_result)
	return solve_helper(K, N, a, c, i+1)





line_1 = "3 5"
line_2 = "1 1 1"
line_3 = "1 2 3"
"""
line_1 = raw_input()
line_2 = raw_input()
line_3 = raw_input()
"""
startTime = datetime.now()
print solve_recurrences(line_1, line_2, line_3)
endTime = datetime.now()
print (endTime - startTime).total_seconds()