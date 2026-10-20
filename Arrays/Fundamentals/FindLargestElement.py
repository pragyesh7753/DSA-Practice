# Find largest element in an array

def largest_element(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest


arr = list(map(int, input("Enter array elements separated by comma: ").split(",")))
print(largest_element(arr))
