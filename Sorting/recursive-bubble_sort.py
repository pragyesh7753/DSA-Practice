def bubble_sort(arr, n):
    if n == 1:
        return

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    bubble_sort(arr, n - 1)


arr = list(map(int, input("Enter array elements separated by comma: ").split(",")))
bubble_sort(arr, len(arr))
print(arr)
