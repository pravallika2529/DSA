# to find the minimum number in a list

lst = [2, 5, 3, 8, 6, 4, 1, 7]

mini = lst[0]
for item in lst:
    if item < mini:
        mini = item
print("The minimum number is: ", mini)

# time complexity --> O(n)
# space complexity --> O(1) --> only 1 variable used (mini)

# no other optimized way