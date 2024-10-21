my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n-1):
    for j in range(n-1-i):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]


print("Sorted array: ", my_array)

'''Improved program: If the array is sorted after first loop or before going through all the loop then the algorithm 
would stop. If the algorithm goes through the array one time without swapping any values, the array must be finished 
sorted, and we can stop the algorithm'''

my_array = [7, 3, 9, 12, 11]

n = len(my_array)
for i in range(n-1):
    swapped = False     # assigning false every time new loop starts
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True  # If any swapping happens then it would assign true which means the array must be still unsorted
    if not swapped:     # if it didn't do any swapping, it means the array is already sorted and no need to go through any more loop.
        break

print("\nImproved program:\nSorted array:", my_array)


