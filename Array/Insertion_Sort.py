my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1, n):
    insert_index = i
    current_value = my_array.pop(i)
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            insert_index = j
    my_array.insert(insert_index, current_value)

print("Sorted array:", my_array)

'''
The above method requires so many shifting during the pop and insert operation. So the improved method below
reduces the shifting and also reduces the loop by copying the current value and stopping the look after finding
the right position for the current value.
'''

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1, n):
    insert_index = i
    current_value = my_array[i]  # copying so that rest of the value doesn't need to shift left.
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]  # copying to the right if any value is greater than current value.
            insert_index = j
        else:       # stopping the loop if program encounters any value to smaller than current value.
            break
    my_array[insert_index] = current_value  # replacing the position with the current value.


print("Sorted array:", my_array)


'''
The first program works by shifting and the second program does only only copy and replace so there no need
shifting operation.
'''