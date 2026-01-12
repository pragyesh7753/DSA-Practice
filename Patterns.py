'''
****
****
****
****
for i in range(4):
    for j in range(4):
        print("*", end="")
    print()
'''

'''
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
'''

'''
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
'''

'''
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
'''

'''
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
'''

'''
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
'''        

'''
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
'''
