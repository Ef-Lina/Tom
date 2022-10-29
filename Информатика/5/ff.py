def Fib(n):
	prev = 0
	nex = 1
	while (n > 0):
		yield prev
		prev, nex = nex, prev+nex
		n -= 1
# вывод с 0 до n
print(list(Fib(6)))