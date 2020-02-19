#Given February 9th, 2020

#Implement a stack that has the following methods:

#push(val), which pushes an element onto the stack
#pop(), which pops off and returns the topmost element of the stack.
#If there are no elements in the stack, then it should throw an error or return null.
#max(), which returns the maximum value in the stack currently.
#If there are no elements in the stack, then it should throw an error or return null.

#Each method should run in constant time.

class EmptyStackError(Exception):
    pass

class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            raise EmptyStackError
        
        return self.stack.pop()
    
    def max(self):
        if len(self.stack) == 0:
            raise EmptyStackError
        
        return max(self.stack)


if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.push(1)
    print(s)
    print(s.max())

    t = Stack()
    print(t)
    t.pop()
    t.max()
