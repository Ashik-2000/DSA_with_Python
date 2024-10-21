my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)


for i in range (n-1):
    swapped = False
    for j in range (n-1-i):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        break

print(my_array)


for i in range(n-1):
    minindex = i
    for j in range(i+1, n-1):
        if my_array[j] < my_array[minindex]:
            minindex = j
    my_array[i], my_array[minindex] = my_array[minindex], my_array[i]

print(my_array)