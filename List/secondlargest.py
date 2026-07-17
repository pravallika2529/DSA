# to find the second largest number in a given list

# BRUTE FORCE WAY
lst = [2, 5, 3, 8, 4, 6, 9]
max_num = lst[0]
sec_max = lst[0]

for num in lst:
    if num > max_num:
        max_num = num

for num in lst:
    if num > sec_max and num != max_num:
        sec_max = num

print("The second largest number is: ", sec_max)
# in this above brute force way, doesnt work if all elements are same
# time complexity --> O(n+n) = O(n), space complexity --> O(1)

# OPTIMIZED WAY
# instead of using 2 loops, we can only use one to traverse :

# lst = [2, 5, 3, 8, 4, 6, 9]
#
# max_num = float('-inf')
# sec_max = float('-inf')
#
# for num in lst:
#     if num > max_num:
#         sec_max = max_num
#         max_num = num
#     elif num > sec_max and num != max_num:
#         sec_max = num
#
# print(sec_max)
