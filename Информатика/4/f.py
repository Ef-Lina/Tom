import numpy
class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + "]"

    def dist(a, b):
    	return ((b.get_y() - a.get_y()) ** 2 + (b.get_x() - a.get_x()) ** 2) ** 0.5

class Shape:
	def __init__(self, type="Shape"):
		self._type = type
	def __str__(self):
		return str(self._type)
	def area (self):
		return Point.dist(self._point_1, self._point_2) * Point.dist(self._point_2, self._point_3)
	def perimeter (self):
		return Point.dist(self._point_1, self._point_2) + Point.dist(self._point_2, self._point_3) + Point.dist(self._point_3, self._point_4) + Point.dist(self._point_4, self._point_1)


class Сircle(Shape):
	def __init__(self, o, r, type="Сircle"):
		super().__init__(type)
		self._point_o = o
		self._r = r
	def __str__(self):
		return  " ".join([super().__str__(), self._point_o.__str__()]) + " r=" + str(self._r)
	def perimeter (self):
		return 2*(numpy.pi)*self._r
	def area (self):
		return (numpy.pi)*(self._r)**2

class Triangle(Shape):
    def __init__(self, p1, p2, p3, type="Triangle"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
    def __str__(self):
        return " ".join([super().__str__(), self._point_1.__str__(), self._point_2.__str__(), self._point_3.__str__()])
    def perimeter (self):
    	return Point.dist(self._point_1, self._point_2) + Point.dist(self._point_2, self._point_3) + Point.dist(self._point_3, self._point_1)
    def area (self):
    	p = (Triangle.perimeter(self))/2
    	a = Point.dist(self._point_1, self._point_2)
    	b = Point.dist(self._point_2, self._point_3)
    	c = Point.dist(self._point_3, self._point_1)
    	return numpy.sqrt(p*(p-a)*(p-b)*(p-c))

class Rectangle(Shape):
	def __init__(self, p1, p2, p3, p4, type="Rectangle"):
		super().__init__(type)
		self._point_1 = p1
		self._point_2 = p2
		self._point_3 = p3
		self._point_4 = p4
	def __str__(self):
		return " ".join([super().__str__(), self._point_1.__str__(), self._point_2.__str__(), self._point_3.__str__(), self._point_4.__str__()])

class Square(Rectangle):
	def __init__(self, p1, p2, p3, p4, type="Square"):
		super().__init__(p1, p2, p3, p4, type)
	def __str__(self):
		return super().__str__()


class Rhomb(Rectangle):
	def __init__(self, p1, p2, p3, p4, type="Rhomb"):
		super().__init__(p1, p2, p3, p4, type)
	def __str__(self):
		return super().__str__()
	def area (self):
		return Point.dist(self._point_1, self._point_3) * Point.dist(self._point_2, self._point_4)/2 


a = Triangle(Point(), Point(0, 3), Point(4, 0))
b = Сircle(Point(1, 1), 5)
c = Square(Point(), Point(0, 1), Point(1, 1), Point(1,0))
d = Rhomb(Point(), Point(0, 1), Point(1, 1), Point(1,0))
print(a)
print(b)
print(c)
print(b.area())
print(a.perimeter())
print(c.perimeter())
print(d.area())
print(a.area())

	
		