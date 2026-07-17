'''
Simple Number Hashing -----------------------?

n = int(input("Enter number of array elements you want: "))

arr = list(map(int, input("Enter list items separated by comma: ").split(",")))

hash = [0] * n

for num in arr:
    hash[num] += 1

q = int(input("Enter the number of queries you want to put: "))

while q > 0:
    number = int(input("Enter the query items one by one: "))
    q -= 1
    print(hash[number])

'''

'''
Character Hashing
'''
