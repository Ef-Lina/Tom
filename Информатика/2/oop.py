import numpy
class Constellation:
	
	def __init__(self, a, b):
		self._a = a
		self._b = b

	def get_a(self):
		return self._a

	def get_b(self):
		return self._b

	def get(self):
		return self._a, self._b

	def set(self, a, b):
		self._a = a
		self._b = b
	
	def exp(self):
		m = numpy.sqrt((self._a)**2 + (self._b)**2)
		p = (self._a)/m
		if self._b < 0:
			return Constellation(m, -numpy.arccos(p))
		else:
			return Constellation(m, numpy.arccos(p))

	def rexp(self):
		return Constellation(self._a * numpy.cos(self._b), self._a * numpy.sin(self._b))

	def __add__(self, other):
		return Constellation(self._a + other._a, self._b + other._b)

	def __sub__(self, other):
		return Constellation(self._a - other._a, self._b - other._b)

	def __mul__(self, other):
		return Constellation(self._a * other._a - self._b * other._b, self._a * other._b + self._b * other._a)

	def __truediv__(self, other):
		if other._a == 0 and other._b == 0:
			return 'not found'
		else:
			return Constellation((self._a*other._a + self._b*other._b)/((other._a)**2 + (other._b)**2), (self._b*other._a - self._a*other._b)/((other._a)**2 + (other._b)**2))
	
	def __str__(self):
		return str(self._a) + " " + str(self._b)

x = Constellation(1.4142135623730951, -0.7853981633974484)
y = Constellation(1, 1)
z = Constellation(1, 1)
print(x.rexp())
print(y.exp())
print(z*y)
print(y/z)
		