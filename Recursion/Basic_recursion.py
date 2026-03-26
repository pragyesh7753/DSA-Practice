# def recursion(n):
#     if n == 0:
#         return 1
#     else:
#         return n * recursion(n - 1)

# print(recursion(5))


# Print name n times

def print_name(i, n):
    if i>n:
        return
    print("Pragyesh")
    print_name(i+1, n)


print_name(1, 5)