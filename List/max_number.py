# finding the maximum number in a list

# brute force way
lst = [3, 5, 2, 8, 1, 9, 4]
max_num = lst[0]
for item in lst:
    if item > max_num:
        max_num = item

print("The maximum number is: ", max_num)
# time complexity --> O(n) --> this is because the loop visits each element in the list exactly once, so O(n)
# space complexity --> O(1) --> the alg doesnt create another list or use extra memory that grows with the input size
# only one extra variable is used
# hence, the space complexity is O(1)

# this is the optimized way only, cuz all elements need to be checked