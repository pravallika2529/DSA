# to find the sum of all the values of keys in a dictionary

dct = {'a': 2, 'b': 6, 'c': 4, 'd': 8}
total = 0

for value in dct.values():
    total = total + value

print("The sum of all values in a dictionary is: ", total)

# this is the only optimized way
# time complexity --> O(n)
# space complexity --> O(1)

#  we can also use the sum() function, this is more python way
# dct = {'a': 2, 'b': 6, 'c': 4, 'd': 8}
#
# total = sum(dct.values())
#
# print(total)