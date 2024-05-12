class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        return self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            return "Stack is already empty."
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return "Stack is empty."
        return self.stack[-1]
    
    def isEmpty(self):
        return not bool(self.stack)
    
    def size(self):
        if len(self.stack) == 0:
            return "Stack is empty."
        return len(self.stack)
    

mystack = Stack()

mystack.push(2)
mystack.push(1)
mystack.push(3)
mystack.push(4)

print("Stack: ", mystack.stack)
print("Pop: ", mystack.pop())
print("Peek: ", mystack.peek())
print("IsEmpty: ", mystack.isEmpty())
print("Size: ", mystack.size())