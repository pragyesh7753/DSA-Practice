s = input("Enter string: ")

freq = {}

for i in s:
    freq[i] = freq.get(i, 0) + 1

print(freq.items())

max_char = ""
min_char = ""
max_count = 0
min_count = float("inf")   # It gives the infinity

for ch, count in freq.items():
    if count > max_count:
        max_count = count
        max_char = ch

    if count < min_count:
        min_count = count
        min_char = ch

print(f"Highest occuring character is: {max_char}, and frequency is: {max_count}")
print(f"Lowest occuring character is: {min_char}, and frequency is: {min_count}")

"""
Not Allowed in many interviews as it contains python's built-in function
highest = max(freq, key=freq.get)
print("The highest occuring element is: ", highest)

lowest = min(freq, key=freq.get)
print("The lowest occuring element is: ", lowest)
"""