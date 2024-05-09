def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


array = [5, 6, 9, 4, 3, 2, 8]
target_val = 3

result = linearSearch(array, target_val)

if result != -1:
    print(f"The target value is in index {result}.")
else:
    print("The value not found.")
