class Node:
    def __init__(self, value, prev_pointer=None, next_pointer=None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())

class List:
    def __init__(self, collection = None):
        self._start_pointer = None
        self._finish_pointer = None
        self._length = 0

    def __len__(self):
        return self._length

    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(Node(value,self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

    def multiappend(self,*args):
        for value in args:
            if self._length == 0:
                self._start_pointer = Node(value) 
                self._finish_pointer = self._start_pointer  
                self._length = 1                 
            else:
                self._finish_pointer.set_next(Node(value, self._finish_pointer))
                self._finish_pointer = self._finish_pointer.get_next()
                self._length += 1

    def __getitem__(self, i):
        if i < 0 or i > self._length:
            return False

        if i >= self._length/2:
            curr_pointer = self._finish_pointer
            for j in range(self._length, i+1, -1):
                curr_pointer = curr_pointer.get_prev()
            return curr_pointer.get_value()
        else:
            curr_pointer = self._start_pointer
            for j in range(i):
                curr_pointer = curr_pointer.get_next()
            return curr_pointer.get_value()

    def __str__(self):
        arr = []
        for i in range(self._length):
            arr.append(str(self[i]))
        return "[" + ", ".join(arr) + "]"

    def pop(self, i):
        if i < 0 or i >= self._length:
            return False
        else:
            st_point = self._start_pointer
            pv_point = self._start_pointer
            for x in range(i + 1):
                st_point = st_point.get_next()
            for j in range(i - 1):
                pv_point = pv_point.get_next()
            pv_point.set_next(st_point)
            self._length -= 1

        
    def sum(self,other):
        value = other._start_pointer
        for x in range(1, other._length):
            self.append(value.get_value())
            value = value.get_next()
        return self
    
    def __iter__(self):
        return self



A = List()
for i in range(5):
    A.append(i)

B = List()
B.multiappend(1,2,3,4,5,6,7,8,9,10) # проверка multiappend

print(A[3]) # проверка __getitem__ 

print(B.pop(3))

for i in range(A._length):
    print(A[i])
print(A)

print(A.sum(B))
print(B.iter())