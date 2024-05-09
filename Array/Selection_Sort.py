my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n-1):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print("Sorted array:", my_array)

'''
Improved version where we don't need to do any pop and insert operation that causes so many shifting operation
in the array values. Here would simply swap the lowest value with the first position value.
'''
my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n-1):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print("\nImproved Sorted array:", my_array)

'''
We must use the min_index variable to record the index of the lowest value or else we would end up doing
swapping every single time we find any lowest value in a single outer loop.
'''

