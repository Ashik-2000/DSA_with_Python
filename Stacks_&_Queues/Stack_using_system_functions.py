stack = []

# push
stack.append(2)
stack.append(1)
stack.append(3)
stack.append(4)
print("Stack: ",stack)

# pop   
stack.pop(  )           
print("Pop: ",stack)

#peek
print("Peek: ", stack[-1])

#inEmpty
isEmpty = not bool(stack)
print("IsEmpty: ", isEmpty)

#size
print("Length: ", len(stack))