# to find the sum of elements in a list

lst = [8, 7, 11, 29, 5, 6, 15, 10]
add = 0
for item in lst:
    add = add + item

print("The sum is: ", add)

# time complexity --> O(n)
# space complexity --> O(1)
# no other optimized way because have to traverse whole list