# Right rotation of array by k steps
# def rightRotate(arr, k):
#     temp = [0] * len(arr)
#     for i in range(len(arr)):
#         newIndex = (i + k) % len(arr)
#         temp[newIndex] = arr[i]
#     print(temp)


# Time Complexity: O(n)
# Space Complexity: O(n)


# Left rotation of array by k steps
# def leftRotate(arr, k):
#     temp = [0] * len(arr)
#     for i in range(len(arr)):
#         newIndex = (i - k) % len(arr)
#         temp[newIndex] = arr[i]
#     print(temp)


# Right rotate without using a new array
def swap(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rightRotate(arr, k):
    n = len(arr)
    k = k % n
    swap(arr, 0, n - 1) # Reverse the whole array
    swap(arr, 0, k - 1) # Reverse first k elements
    swap(arr, k, n - 1) # Reverse the remaining elements
    print(arr)


rightRotate([1, 2, 3, 4, 5, 6], 2)


def leftRotate(arr, k):
    n = len(arr)
    k = k % n
    swap(arr, 0, k - 1)  # Reverse first k elements
    swap(arr, k, n - 1) # Reverse the remaining elements
    swap(arr, 0, n - 1) # Reverse the whole array
    print(arr)

leftRotate([1, 2, 3, 4, 5, 6], 2)

# Space Complexity: O(1)