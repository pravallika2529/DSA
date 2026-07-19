# count the no. of consonants in a string

# FIRST METHOD - BRUTE FORCE
string = input("Enter a sentence: ")
count = 0

for ch in string.lower():
    if ch not in "aeiou" and ch.isalpha():
        count += 1

print("The no. of consonants is: ", count)
# time complexity --> O(n) --> lower() takes O(n) and for loop runs n times
# space complexity --> O(n), because of the string.lower() it makes a copy

# better way for O(1) space complexity:

# string = input("Enter a sentence: ")
# count = 0
#
# for ch in string:
#     if ch.isalpha() and ch.lower() not in "aeiou":
#         count += 1
#
# print("The no. of consonants is:", count)

# above, we are converting character to lower, not the whole string
# space complexity --> O(1)