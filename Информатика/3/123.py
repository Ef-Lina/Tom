class Node:
    def __init__(self, value,
                 prev_pointer=None, next_pointer=None):
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
            self._finish_pointer.set_next(Node(value,
                                               self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

    def __getitem__(self, i): 
        if i < 0 or i > self._length:
            return False

        elif i >= self._length/2:
            curr_pointer = self._finish_pointer
            for j in range(self._length, i, -1):
                curr_pointer = curr_pointer.get_prev()
            return curr_pointer.get_value()
        else:
            curr_pointer = self._start_pointer
            for j in range(i):
                curr_pointer = curr_pointer.get_next()
            return curr_pointer.get_value()

    def __pop__(self, i): 
        if i < 0 or i >= self._length:
            return False
        
        elif i >= self._length/2:
            curr_pointer = self._finish_pointer
            for j in range(self._length, i, -1):
                curr_pointer = curr_pointer.get_prev()
            return curr_pointer.get_value()
            self[i-1].set_next(self[i+1].get_value())
            self[i+1].set_prev(self[i-1].get_value())
            for j in range (i+1, self._length):
                self[j] = self[j+1]
            self._length -= 1
    def sum(self, other):
        if other._length == 0:
            return self
        else:
            self._finish_pointer.set_next(other._start_pointer())
            for i in range(other._length):
                self._finish_pointer = other[i]
                self._length += 1
            return self


    def __str__(self):
        arr = []
        for i in range(self._length):
            arr.append(str(self[i]))
        return "[" + ", ".join(arr) + "]"


A = List()
for i in range(5):
    A.append(i)
for element in A:
    print(element)
print(A)