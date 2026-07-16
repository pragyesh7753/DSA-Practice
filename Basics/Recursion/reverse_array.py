# Using two pointers

# def reverse(arr, left, right):
#     if left >= right:
#         return arr
#     arr[left], arr[right] = arr[right], arr[left]
#     return reverse(arr, left + 1, right - 1)

# my_arr = [10, 5, 7, 3]
# print(reverse(my_arr, 0, len(my_arr) - 1))

# TC : O(n), SC: O(n)


# Using one variable
def reverse(i, arr, n):
    if i >= n // 2:
        return arr
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return reverse(i + 1, arr, n)


# my_arr = input("Enter list items separated by comma: ").split(",")
my_arr = [10, 5, 7, 3]
print(reverse(0, my_arr, len(my_arr)))

# TC : O(n/2) = O(n), SC: O(n/2) = O(n)
