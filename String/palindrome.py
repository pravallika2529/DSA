# checking if the given string is a palindrome or not

string = input("Enter a string: ")


def palindrome(s):
    for i in range(0, len(s)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


if palindrome(string) is True:
    print("Palindrome")
else:
    print("Not palindrome")

# time complexity --> O(n)
# space complexity --> O(1)

# the above method there can be a small optimization:
# instead of looping from 0 to len(s), looping till half of len(s) is enough
# for i in range(0, (len(s)//2))
# this wont change time/space complexity, but it is more efficient
# if palindrome(string): --> this can be written instead also