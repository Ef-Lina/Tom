def sort(A):
	if len(A) <= 1:
		return A
	else:
		import random
		x = random.choice(A)
		min_A = []
		max_A = []
		x_A = []
		for i in A:
			if i < x:
				min_A.append(i)
			elif i > x:
				max_A.append(i)
			else:
				x_A.append(i)
		return sort(min_A) + x_A + sort(max_A)
