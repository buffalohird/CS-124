from datetime import datetime
import time
import copy

def solve_recurrences(line_1, line_2, line_3):


	K, N = map(int, line_1.split())
	a = map(int, line_2.split())
	c = map(int, line_3.split())

	return solve_helper(K, N, a, c)

	
	
def solve_helper(K, N, a, c):

	i = K
	matrix = []
	matrix.append(c)
	index = 0
	matrix_width = len(c)
	for item_a in reversed(a[1:]):
		new_list = [0] * matrix_width
		new_list[index] = 1
		index += 1
		matrix.append(new_list)

	for item in matrix:
		print item
	print " "

	matrix_a = [a[::-1]]
	#print matrix_a
	old_matrix = copy.copy(matrix)
	while i < N:
		print i
		matrix = matrix_multiply(old_matrix, matrix)
		i += 1

		test_matrix = matrix_multiply(matrix, matrix_a)
		for item in old_matrix:
			print item

		print "\n\n"

	return matrix_multiply(matrix, matrix_a)[0][0] % 1000


def matrix_multiply(a,b):
    zip_b = b
    if len(b) != 1:
        zip_b = zip(*b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a]




"""
	new_result_list = zip(reversed(a), c)
	new_result = reduce(lambda sum, (x, y): sum + x*y, new_result_list, 0)
	a.append(new_result)
	return solve_helper(K, N, a, c, i+1)
"""





line_1 = "2 100"
line_2 = "12 17"
line_3 = "9 15"

"""
line_1 = raw_input()
line_2 = raw_input()
line_3 = raw_input()
"""

startTime = datetime.now()
print solve_recurrences(line_1, line_2, line_3)
endTime = datetime.now()
#print (endTime - startTime).total_seconds()




