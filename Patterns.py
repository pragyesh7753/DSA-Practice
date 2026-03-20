"""
Pattern 1
****
****
****
****
for i in range(4):
    for j in range(4):
        print("*", end="")
    print()
"""

"""
Pattern 2
*
**
***
****
*****
num = int(input("Enter a number: "))
def pattern(num):
    for i in range(num + 1):
        for j in range(i):
            print("*", end="")
        print()
        
pattern(num)
"""

"""
Pattern 3
1
12
123
1234
12345
def pattern(num):
    for i in range(num + 1):
        for j in range(i):
            print(j ,end="")
        print()
        
pattern(6)
"""

"""
Pattern 4
1
22
333
4444
55555

def pattern(num):
    for i in range(num + 1):
        for j in range(i):
            print(i, end="")
        print()

pattern(6)
"""

"""
Pattern 5
*****
****
***
**
*

def pattern(num):
    for i in range(1, num + 1):
        for j in range(1, num - i + 2):
            print("*", end ="")
        print()
"""

"""
Pattern 6
12345
1234
123
12
1

def pattern(num):
    for i in range(1, num + 1):
        for j in range(1, num - i + 2):
            print(j, end = "")
        print()
"""

"""
Pattern 7
    *
   ***
  *****
 *******
*********
def pattern(num):
    for i in range(1, num + 1):
        for j in range(num - i): # print spaces
            print(" ", end="")
        for k in range(2 * i - 1): # print stars
            print("*", end="")
        print()
"""

"""
Pattern 8
*********
 *******
  *****
   ***
    *

def pattern(num):
            for i in range(num):
                for j in range(i):
                    print(" ", end = "")
                for k in range(2 * (num - i) - 1):
                    print("*", end = "")
                print()
"""

"""
Pattern 9
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
def pattern(num):
    for i in range(1, 2 * num):
        if i <= num:
            stars = 2 * i - 1
            spaces = num - i
        else:
            stars = 2 * (2 * num - i) - 1
            spaces = i - num
        print(" " * spaces + "*" * stars)
"""

"""
Pattern 10
*
**
***
****
*****
****
***
**
*

def pattern(num):
    for i in range(1, 2 * num):
        if i <= num:
            stars = i
        else:
            stars = 2 * num - i
        print("*" * stars) 
"""

"""
Pattern 10
1
01
101
0101
10101
def pattern(num):
    start = 1
    for i in range(num):
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(i + 1):
            print(start, end="")
            start = 1 - start
        print()
 """

"""
Pattern 12
1                    1
12               21
123          321
1234     4321
1234554321
def pattern(num):
    space = 2 * (num - 1)
    for i in range(1, num + 1):
        # left numbers
        for j in range(1, i + 1):
            print(j, end="")

        # spaces
        for j in range(space):
            print(" ", end="")

        # right numbers
        for j in range(i, 0, -1):
            print(j, end="")

        print()
        space -= 2
"""


# number
pattern(5)
