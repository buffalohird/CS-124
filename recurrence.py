import copy

def solve_recurrences(line_1, line_2, line_3):


	K, N = map(int, line_1.split())
	a = map(int, line_2.split())
	c = map(int, line_3.split())

	if(N < 1):
		i = len(a) - 1
		return solve_helper_old(K, N, a, c, i)

	return solve_helper(K, N, a, c)

	
	
def solve_helper(K, N, a, c):

	i = 1
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
	matrix_list.append(matrix)
	matrix_bool = False
	
	while i < N - K + 1:
		if i * 2 < N - K + 1:
			matrix = matrix_multiply(matrix, matrix)
			i += i
			matrix_list.append(matrix)
		else:
			for item in reversed(matrix_list):	
				index = matrix_list.index(item)
				if i + 2 ** index < N - K + 2:
					matrix = matrix_multiply(matrix, item)
					i += 2 ** index
					break
				else:
					matrix_list.pop(index)
		
		for item in matrix_list:
			for row in item:
				print row
			print ""
		print ""
		


	return matrix_multiply(matrix, matrix_a)[0][0] % 1000


# old, non-matrix solution
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
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) % 1000 for col_b in zip_b] for row_a in a]



"""
line_1 = "2 100"
line_2 = "12 17"
line_3 = "9 15"
"""
line_1 = raw_input()
line_2 = raw_input()
line_3 = raw_input()







print solve_recurrences(line_1, line_2, line_3)




