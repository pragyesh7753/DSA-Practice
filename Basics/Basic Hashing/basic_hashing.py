"""
Simple Number Hashing ----------------------->

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

"""

"""
Character Hashing ------------------------------------->

s = input("Enter your string here: ").strip()

hash = [0] * 256

for i in s:
    hash[ord(i)] += 1

q = int(input("Enter number of queries here: "))

for _ in range(q):
    c = input("Enter character: ").strip()
    print(hash[ord(c)])
"""

"""
Better Approach using Dictionary for Number Array ------------------>
arr = list(map(int, input("Enter list separated by comma: ").split(",")))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print(freq)

q = int(input("Tell me, how much queries you want to put in numbers: "))

while q > 0:
    number = int(input("Enter the list items one by one: "))
    print(freq.get(number, 0))
    q -= 1
"""

"""
Better Approach using collections.defaultdict for Number Array ------------------>

from collections import defaultdict

arr = list(map(int, input("Enter the list items separated by comma: ").split(",")))

freq = defaultdict(int)

for num in arr:
    freq[num] += 1

q = int(input("Tell me, how much queries you wanna put in numbers: "))

while q > 0:
    number = int(input("Enter the query items one by one: "))
    print(freq[number])  # Returns 0 automatically if the key doesn't exist
    q -= 1

print(freq)

# But here's the catch in defaultdict method, that it creates entry in defaultdict, even when you read it
"""

"""
Better Approach using Dictionary for Character Array ------------------>
s = input("Enter a string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

q = int(input("Enter the number, how many queries you wanna put: "))

while q > 0:
    str = input("Enter the characters one by one you wanna search for: ")
    print(freq.get(str, 0))
    q -= 1

print(freq)    # To print the frequency dictionary
"""
