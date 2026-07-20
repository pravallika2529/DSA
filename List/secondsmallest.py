# to find the second smallest number in a list

lst = [2, 5, 3, 8, 4, 6, 9]

min_num = float('inf')
sec_min = float('inf')

for num in lst:
    if num < min_num:
        sec_min = min_num
        min_num = num
    elif num != min_num and num < sec_min:
        sec_min = num
print("Second smallest number in list: ", sec_min)

# float('inf') is used to initialize the second smallest value
# because it is larger than any number.
# This ensures that the first valid number smaller than infinity
# updates sec_min, allowing the algorithm to work correctly.

# time complexity --> O(n)
# space complexity --> O(1)
