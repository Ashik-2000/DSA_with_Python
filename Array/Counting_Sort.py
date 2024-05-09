def countingSort(array):
    max_val = max(array)
    count = [0] * (max_val+1)

    while len(array) > 0:
        value = array.pop()
        count[value] += 1

    for i in range(len(count)):
        while count[i] > 0:
            array.append(i)
            count[i] -= 1

    return array


unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = countingSort(unsortedArr)
print("Sorted array:", sortedArr)
