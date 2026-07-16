def reverse(n):
    revNum = 0
    while n > 0:
        lastDigit = n % 10
        revNum = (revNum * 10) + lastDigit
        n = n // 10
    return revNum


def palindrome(n):
    return n == reverse(n)

print(palindrome(12321))