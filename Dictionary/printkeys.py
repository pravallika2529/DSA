# to print all the keys of a dictionary

dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

for key in dct:
    print(key, end=" ")

# time complexity --> O(n)
# space complexity --> O(1)
# every key must be visited so this is the only TC --> O(n)