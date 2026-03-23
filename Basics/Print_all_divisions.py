# def divisions(n):
#     for i in range(1, n):
#         if n % i == 0:
#             print(i)


# Alternative method
from math import sqrt


def divisions(n):
    smallNum = []
    largeNum = []
    # for i in range(1, int(sqrt(n) + 1)):
    i = 1
    while i * i <= n:    #slightly better approach as it avoids sqrt(n) function calculation
        if n % i == 0:
            smallNum.append(i)
            if n // i != i:
                largeNum.append(n // i)
        i += 1
    print(*(smallNum + largeNum[::-1]))


divisions(36)
