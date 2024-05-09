def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftPart = arr[:mid]
    rightPart = arr[mid:]

    leftPortion = mergeSort(leftPart)
    rightPortion = mergeSort(rightPart)

    return merge(leftPortion, rightPortion)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


myArray = [3, 7, 6, -10, 15, 23.5, 55, -13]
result = mergeSort(myArray)
print(f"Sorted array: {result}")
