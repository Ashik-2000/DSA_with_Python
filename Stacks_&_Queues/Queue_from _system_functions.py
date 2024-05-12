queue = []

# push
queue.append(2)
queue.append(1)
queue.append(3)
queue.append(4)
print("Queue: ",queue)

# pop   
queue.pop(0)           
print("dequeue: ",queue)

#peek
print("Peek: ", queue[0])

#inEmpty
isEmpty = not bool(queue)
print("IsEmpty: ", isEmpty)

#size
print("Length: ", len(queue))