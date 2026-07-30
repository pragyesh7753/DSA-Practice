def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j

        # Actually this step(if-condition) is a check that if array is already sorted, as if array is already sorted then doing the whole operation has no worth
        if mini != i:
            arr[i], arr[mini] = arr[mini], arr[i]


elements = list(map(int, input("Enter array elements separated by comma: ").split(",")))

selection_sort(elements)
print(f"The sorted array is: {elements}")
