# checking whether a substring is present in a given string

# brute force way
string = input("Enter a string: ")
substring = input("Enter a substring: ")

if substring in string:
    print("Substring is present")
else:
    print("Substring is not present")
# time complexity --> O(nxm)
# where, n --> length of main_string, m --> length of sub_string
# the sub_string is compared at multiple positions of the main string

# space complexity --> O(1)
# only a couple of variables (string and substring) are used
# no extra data structure is created that grows with the input size

# there is no other efficient and optimized method