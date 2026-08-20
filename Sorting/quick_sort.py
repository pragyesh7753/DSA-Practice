import random


def quick_sort(arr, low, high):
    if low <= high:
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while i <= j:
        # Find an element greater than pivot
        while i <= high and arr[i] >= pivot:
            i += 1

        # Find an element lesser than pivot
        while j >= low and arr[j] < pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Put pivot element in its correct position
    arr[low], arr[j] = arr[j], arr[low]
    return j


# But here is the better randomized pivot selection
# def partition(arr, low, high):
#     random_index = random.randint(low, high)

#     # Move the pivot element to last
#     arr[random_index], arr[high] = arr[high], arr[random_index]
#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]

#     # Put pivot in correct position
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]

#     return i + 1


arr = list(map(int, input("Enter array elements spearated by comma: ").split(",")))
print(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)

"""
Time Complexity - O(nlogn) (Best & Average Case), O(n^2) (Worst Case)
Space Complexity - O(1)
"""
