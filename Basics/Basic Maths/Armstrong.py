def armstrong(n):
    sum = 0
    revNum = n
    while revNum > 0:
        lastDigit = revNum % 10
        sum += lastDigit ** len(str(n))
        revNum = revNum // 10
    return sum == n


print(armstrong(1634))
