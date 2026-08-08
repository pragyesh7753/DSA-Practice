def insertion_sort(arr, i, n):
    if i == n:
        return

    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1

    insertion_sort(arr, i + 1, n)


arr = list(map(int, input("Enter array elements separated by comma: ").split(",")))
sorted = insertion_sort(arr, 0, len(arr))
print(arr)
