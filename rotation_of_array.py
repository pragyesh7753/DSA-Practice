# Right rotation of array by k steps
def rightRotate(l1, k):
    temp = [0] * len(l1)
    for i in range(len(l1)):
        newIndex = (i + k) % len(l1)
        temp[newIndex] = l1[i]
    print(temp)


rightRotate([1, 2, 3, 4, 5, 6], 4)
# Time Complexity: O(n)
# Space Complexity: O(n)


# Left rotation of array by k steps
def leftRotate(l1, k):
    temp = [0] * len(l1)
    for i in range(len(l1)):
        newIndex = (i - k) % len(l1)
        temp[newIndex] = l1[i]
    print(temp)


leftRotate([1, 2, 3, 4, 5, 6], 3)
