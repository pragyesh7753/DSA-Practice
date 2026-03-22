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
Pattern 11
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

"""
Pattern 13
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15

def pattern(num):
    n = 1
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(n, end=" ")
            n = n + 1
        print()
"""

"""
Pattern 14
A 
A B
A B C
A B C D
A B C D E

def pattern(num):
    for i in range(num):
        for j in range(i + 1):
            print(chr(65 + j), end=" ")
        print()
"""

"""
Pattern 15
A B C D E 
A B C D
A B C
A B
A

def pattern(num):
    for i in range(num):
        for i in range(num - i ):
            print(chr(65 + i), end=" ")
        print()
"""
"""
Pattern 16
A 
B B
C C C
D D D D
E E E E E

def pattern(num):
    for i in range(num):
        for j in range(i + 1):
            print(chr(65 + i), end=" ")
        print()
"""


"""
Pattern 17
            A 
         A B A
      A B C B A
   A B C D C B A
A B C D E D C B A

def pattern(num):
    for i in range(1, num + 1):
        # spaces
        for j in range(num - i):
            print(" ", end=" ")

        # increasing characters
        for j in range(i):
            print(chr(65 + j), end=" ")

        # decreasing characters
        for j in range(i - 2, -1, -1):
            print(chr(65 + j), end=" ")

        print()
"""

"""
Pattern 18
E 
D E
C D E
B C D E
A B C D E 

def pattern(num):
    for i in range(num):
        for j in range(num - i - 1, num):
            print(chr(65 + j), end=" ")
        print()
"""

"""
Pattern 19
**********
****    ****
***        ***
**            **
*                *
*                *
**            **
***        ***
****    ****
**********

def pattern(num):
    spaces = 0
    for i in range(num):
        # stars
        for j in range(num - i):
            print("*", end="")
        # spaces
        for j in range(spaces):
            print(" ", end="")

        # stars
        for j in range(num - i):
            print("*", end="")

        spaces += 2
        print()

    spaces = 2 * num - 2
    for i in range(num):
        # stars
        for j in range(i + 1):
            print("*", end="")
        # spaces
        for j in range(spaces):
            print(" ", end="")
        # stars
        for j in range(i + 1):
            print("*", end="")

        spaces -= 2
        print()
"""

"""
Pattern 20
*                *
**            **
***        ***
****    ****
**********
****    ****
***        ***
**            **
*                *

def pattern(num):
    for i in range(1, num + 1):
        # left stars
        for j in range(i):
            print("*", end="")

        # spaces
        for j in range(2 * (num - i)):
            print(" ", end="")

        # right stars
        for j in range(i):
            print("*", end="")
        print()

    # lower part
    for i in range(num - 1, 0, -1):
        # left stars
        for j in range(i):
            print("*", end="")

        # spaces
        for j in range(2 * (num - i)):
            print(" ", end="")

        # right stars
        for j in range(i):
            print("*", end="")
        print()
"""

"""
Pattern 21
*****
*      *
*      *
*      *
*****

def pattern(num):
    for i in range(num):
        for j in range(num):
            if i == 0 or j == 0 or i == num - 1 or j == num - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
"""

"""
Pattern 22
4 4 4 4 4 4 4 
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4

def pattern(num):
    for i in range(2 * num - 1):
        for j in range(2 * num - 1):
            top = i
            left = j
            right = (2 * num - 2) - j
            bottom = (2 * num - 2) - i
            print(num - min(top, left, right, bottom), end=" ")
        print()
"""



# pattern(4)
