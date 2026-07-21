# invert keys and values in a dictionary

# BRUTE FORCE WAY
old_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
new_dict = {}

for key, value in old_dict.items():
    new_dict[value] = key

print(new_dict)

# time complexity --> O(n)
# space complexity --> O(n) --> because new dictionary's size keeps increasing
# the above method only works if all values are unique

# there is no other optimized way
