# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1,n):
#         j = i
#         while j > 0 and arr[j - 1] > arr[j]:
#             arr[j - 1], arr[j] = arr[j], arr[j - 1]
#             j -= 1
#     return arr


# More efficient approach
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


arr = list(map(int, input("Enter list items separated by comma: ").split(",")))
print(f"The sorted array is: {insertion_sort(arr)}")
