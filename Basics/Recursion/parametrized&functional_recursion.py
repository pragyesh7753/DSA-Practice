def parameterized_recursion(i, sum):
    if i == 0:
        print(sum)
        return
    parameterized_recursion(i - 1, sum + i)


parameterized_recursion(3, 0)


def functional_recursion(n):
    if n == 0:
        return 0

    return n + functional_recursion(n - 1)


print(functional_recursion(3))

# More efficient among these two recursion ways is the parameterized way because it uses tail recursion and avoids the overhead of maintaining multiple stack frames. In contrast, functional recursion builds up a call stack that can lead to increased memory usage and potential stack overflow for large input values.
