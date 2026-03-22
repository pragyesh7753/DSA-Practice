from math import log10


def extract_digits(n):
    # count = 0
    # while n > 0:
    #     # lastDigit = n % 10
    #     count = count + 1
    #     n = n // 10

    # Another way to count digits
    count = int(log10(n)) + 1
    return count


print(extract_digits(129345))
