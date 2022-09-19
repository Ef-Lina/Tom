def fib(n):
		f1 = 1
		f2 = 1
		fi = 0
		if n == 1 or n == 2:
			return 1
		else:
			for i in range (2, n) :
				fi = f1 + f2
				n -= 1
				f1 = f2
				f2 = fi
			return f2

print(fib(6))
