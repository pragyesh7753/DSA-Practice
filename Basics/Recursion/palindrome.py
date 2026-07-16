def palindrome(i, str):
    if i >= len(str) // 2:
        return True
    if str[i] != str[len(str) - i - 1]:
        return False
    return palindrome(i + 1, str)


# str = "madam"
print(palindrome(0, "madsm"))

# TC : O(n/2) = O(n), SC: O(n/2) = O(n)
