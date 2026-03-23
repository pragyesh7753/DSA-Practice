# def  isPrime(n):
#     counter = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             counter += 1
#     return counter == 2


# Alternative method
def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True


print(isPrime(17))


def primeNumbers(n):
    for i in range(2, n + 1):
        if isPrime(i):
            print(i, end=" ")


primeNumbers(100)