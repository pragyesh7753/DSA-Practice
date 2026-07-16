# GCD - Greatest Common Divisor

# Bruteforce method to find GCD of two numbers
# def gcd(n1, n2):
#     gcd = 1
#     for i in range(1, min(n1, n2) + 1):
#         if n1 % i == 0 and n2 % i == 0:
#             gcd = i
#     return gcd


def gcd(n1, n2):
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1

    if n1 == 0:
        return n2

    return n1


print(gcd(52, 120))
