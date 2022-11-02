import numpy
import numbers
class Constellation:
	a = input()
	b = input()
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
		print('oot')
		
	
	def exp(self):
		if self._b == 0 and self._a == 0:
			return Constellation(self._a,self._b)
		else:
			m = numpy.sqrt((self._a)**2 + (self._b)**2)
			p = (self._a)/m
			if self._b < 0:
				return Constellation(m, -numpy.arccos(p))
			else:
				return Constellation(m, numpy.arccos(p))

	def rexp(self):
		return Constellation(self._a * numpy.cos(self._b), self._a * numpy.sin(self._b))

	def __abs__(self):
		m = numpy.sqrt((self._a)**2 + (self._b)**2)
		return m

	def __add__(self, other):
		if isinstance(other, numbers.Number):
			return Constellation(self._a + other, self._b)
		elif isinstance(other, Constellation):
			return Constellation(self._a + other._a, self._b + other._b)
		else:
			return 'not found'

	def __sub__(self, other):
		if isinstance(other, numbers.Number):
			return Constellation(self._a - other, self._b)
		elif isinstance(other, Constellation):
			return Constellation(self._a - other._a, self._b - other._b)
		else:
			return 'not found'

	def __mul__(self, other):
		if isinstance(other, numbers.Number):
			return Constellation(self._a * other, self._b * other)
		elif isinstance(other, Constellation):
			return Constellation(self._a * other._a - self._b * other._b, self._a * other._b + self._b * other._a)
		else:
			return 'not found'

	def __truediv__(self, other):
		if isinstance(other, numbers.Number):
			return Constellation(float(self._a / other), float(self._b / other))
		elif isinstance(other, Constellation):
			if other._a == 0 and other._b == 0:
				raise ValueError ('Деление на 0')
			else:
				return Constellation((self._a*other._a + self._b*other._b)/((other._a)**2 + (other._b)**2), (self._b*other._a - self._a*other._b)/((other._a)**2 + (other._b)**2))
		else:
			return 'not found'

	def __str__(self):
		return str(self._a) + " + i*(" + str(self._b) + ")"


	def __eq__(self, other):
		if isinstance(other, numbers.Number):
			if self._a == other and self._b == 0:
				return True
			else:
				return False
		if isinstance(other, Constellation):
			if elf._a == other._a and self._b == other._b:
				return True
			else:
				return False
	

	def __getitem__(self, item):
		if item == 0:
			return self._a
		elif item == 1:
			return self._b
		else:
			return 'not found'

	def __setitem__(self, key, value):
		if key == 0:
			self._a = value
		elif key == 1:
			self._b = value



s = Constellation(3,4)
#d = Constellation(3,4)
#g = 2
#print(s/g)
print(s[1])
#print(abs(d))