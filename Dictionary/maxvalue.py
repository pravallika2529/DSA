# we have to find the key in the dictionary with the maximum value

dct = {'a': 5, 'b': 2, 'c': 4, 'd': 8, 'e': 1}

max_value = dct['a']
max_key = 'a'
for key, value in dct.items():
    if value > max_value:
        max_value = value
        max_key = key

print("The key with the maximum value is: ", max_key)
print("The value of this key(max) is: ", max_value)

# time complexity --> O(n)
# space complexity --> O(1) --> only 2 extra variables are used

# another way to initialize the max key and value is,
# first_key = list(dct.keys())[0]
# max_key = first_key
# max_value = dct[first_key]