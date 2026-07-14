# to reverse a string

# BRUTE FORCE WAY
org_str = input("Enter a string: ")
reversed_str = ""
for ch in org_str[::-1]:
    reversed_str += ch

print("The reversed string is: ", reversed_str)
# time complexity --> O(n^2)
# space complexity --> O(n)
# this is because we introduce a new string, and its size grows till 'n'

# strings are immutable, we can only concatenate 2 string
# hence, we do str += ch, we don't do str[i] = ch X

# OPTIMIZED WAY
# org_str = input("Enter a string: ")
# reversed_str = org_str[::-1]
#
# print("The reversed string is:", reversed_str)

# for the above optimized way, TC --> O(n), SC --> O(n)

# *** for string concatenation, the time complexity will be O(n)
# this is because new copy of string is created every time we add character
# old string gets discarded
