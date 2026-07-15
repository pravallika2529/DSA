# to merge two dictionaries into one

dct1 = {'a': 1, 'b': 2, 'c': 3}
dct2 = {'d': 4, 'e': 5, 'f': 6}

dct = {}

for key1, value1 in dct1.items():
    dct[key1] = value1

for key2, value2 in dct2.items():
    dct[key2] = value2

print("The merged dictionary is: ", dct)

# time complexity --> O(n+m)
# space complexity --> O(n+m) --> since new dct increases till n+m

# another way is, we can just loop through the keys and assign the keys in new dct
# we don't have to give values also, just keys is enough

# METHOD 2:

# dct = {}
#
# for key in dct1:
#     dct[key] = dct1[key]
#
# for key in dct2:
#     dct[key] = dct2[key]
#
# print(dct)