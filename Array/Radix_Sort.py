myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Unsorted array: ", myArray)
radix = [[], [], [], [], [], [], [], [], [], []]
max_val = max(myArray)
exp = 1

while max_val // exp > 0:

    while len(myArray):
        value = myArray.pop()
        rad_index = (value // exp) % 10
        radix[rad_index].append(value)

    for bucket in radix:
        while len(bucket) > 0:
            value = bucket.pop()
            myArray.append(value)

    exp *= 10


print("Sorted array: ", myArray)
