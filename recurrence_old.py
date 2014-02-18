import copy

def solve_recurrences(line_1, line_2, line_3):


	K, N = map(int, line_1.split())
	a = map(int, line_2.split())
	c = map(int, line_3.split())

	if(N < 5):
		i = len(a) - 1
		return solve_helper_old(K, N, a, c, i)

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

	matrix_a = [a[::-1]]
	old_matrix = copy.copy(matrix)
	matrix_list = []
	matrix_bool = False
	for item in matrix:
		print item
	while i < N:
		if 1 == 2:#i * 2 < N:
			matrix = matrix_multiply(matrix, matrix)
			i += i - 1
			matrix_list.append(matrix)
		else:
			"""
			for item in reversed(matrix_list):
				print matrix_list
				index = matrix_list.index(item) + 1
				matrix_bool = False
				if i + 2 ** index < N:
					matrix = matrix_multiply(matrix, item)
					i += index
					matrix_bool = True
					break"""

			if matrix_bool == False:
				matrix = matrix_multiply(old_matrix, matrix)
				i += 1

		print i 
		for item in matrix:
			print item

		print ""

	print matrix_a
	return matrix_multiply(matrix, matrix_a)[0][0] % 1000


def solve_helper_old(K, N, a, c, i):
	if i == N:
		return a.pop() % 1000

	new_result_list = zip(reversed(a), c)
	new_result = reduce(lambda sum, (x, y): sum + x*y, new_result_list, 0)
	a.append(new_result)
	return solve_helper_old(K, N, a, c, i+1)


def matrix_multiply(a,b):
    zip_b = b
    if len(b) != 1:
        zip_b = zip(*b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a]




line_1 = "3 5"
line_2 = "1 2 3"
line_3 = "3 2 1"
"""
line_1 = raw_input()
line_2 = raw_input()
line_3 = raw_input()
"""


print solve_recurrences(line_1, line_2, line_3)



