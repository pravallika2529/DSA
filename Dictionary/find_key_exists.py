# given a dictionary, we have to find if a certain key exists in it

# brute force way:
dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key = input("Enter the search key: ")

if key in dct.keys():
    print("The key is present")
else:
    print("Key is not present")

# instead of using the dict.keys() function, there is another method
# by default 'in' checks the keys, so we can just use that
# --> 'if key in dct:' can replace the previous condition

# time complexity --> O(n)
# this is because python dicts are implemented using a hash table
# therefore, direct access to keys --> O(1) --> average case
# if O(n), this is due to collisions (very rare case)

# space complexity --> O(1) --> 'key' variable

