def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = list(map(int, input("Enter array elements separated by comma: ").split(",")))

print(bubble_sort(arr))
