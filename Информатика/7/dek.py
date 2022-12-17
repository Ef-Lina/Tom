import time
from functools import lru_cache
def o_decorator(func):
    def another(*args):
        return func(*args[::-1])
    return another

def arg_decorator(func):
	def strok(*args):
		return str(func(*args)) + "\n" + str(args)
	return strok

@o_decorator
def foo(*args):
	for x in args:
		return args

def fo(*args):
	for x in args:
		return args
@arg_decorator
def fon(*args):
	a = 0
	for x in args:
		a += int(x)
	return a

def error_decorator(func):
    def wrapped(*args):
        try:
            return func(*args)
        except Exception as e:
            return "Error:", e
    return wrapped

@error_decorator
def div(a, b):
	c = int(a)/int(b)
	return c

def time_decorator(func):
    def wrapper(*args, **kwargs):

        start_time = time.time()
        res = func(*args, **kwargs)
        return time.time() - start_time
    return wrapper



@time_decorator
def fib1(n):
    if n == 0 or n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)
@time_decorator
@lru_cache(maxsize=None)
def fib2(n):
    if n == 0 or n == 1:
        return 1
    return fib2(n - 1) + fib2(n - 2)
@time_decorator
def fibc1(n):
	fib1 = 1
	fib2 = 1
	i = 0
	while i < n - 2:
		fib_sum = fib1 + fib2
		fib1 = fib2
		fib2 = fib_sum
		i = i + 1
	return fib2
@time_decorator
@lru_cache(maxsize=None)	
def fibc2(n):
	fib1 = 1
	fib2 = 1
	i = 0
	while i < n - 2:
		fib_sum = fib1 + fib2
		fib1 = fib2
		fib2 = fib_sum
		i = i + 1
	return fib2
def fast_decorator(func):
	def wrapper(*args):
		if fib1(*args) > fib2(*args):
				return 'С lru_cache быстрее'
		elif fib2(*args) > fib1(*args):
				return 'Без lru_cache быстрее'
		else:
			return 'Одинаково'
	return wrapper
def fastсr_decorator(func):
	def wrapper(*args):
		if fibc1(*args) > fib1(*args):
				return 'Рекурсия быстрее'
		elif fib1(*args) > fibc1(*args):
				return 'Цикл быстрее'
		else: 
				return 'Одинаково'
	return wrapper

@fast_decorator
def Fib(n):
	return fib1(n)

@fastсr_decorator
def Fibc(n):
    return fibc1(n)


print(foo(4, 5))
print(fo(5, 4))
print(fon(1, 2, 3))
print(div(2, 1))
print(div(2, 0))
print(Fib(30))
print(Fibc(30))
