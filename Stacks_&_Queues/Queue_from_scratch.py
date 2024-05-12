class Queue:
    def __init__(self):
        self.queue = []

    def push(self, element):
        return self.queue.append(element)

    def pop(self):
        if len(self.queue) == 0:
            return "Queue is already empty."
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return "Queue is empty."
        return self.queue[0]
    
    def isEmpty(self):
        return not bool(self.queue)
    
    def size(self):
        if len(self.queue) == 0:
            return "Queue is empty."
        return len(self.queue)
    

mystack = Queue()

mystack.push(2)
mystack.push(1)
mystack.push(3)
mystack.push(4)

print("Queue: ", mystack.queue)
print("Dequeue: ", mystack.pop())
print("Peek: ", mystack.peek())
print("IsEmpty: ", mystack.isEmpty())
print("Size: ", mystack.size())