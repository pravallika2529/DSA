# to search for an element in a list

lst = [5, 2, 4, 3, 7, 9, 8]
key = int(input("Enter key: "))
isFound = 0

for item in lst:
    if item == key:
        isFound = 1
        break

if isFound:
    print("Found")
else:
    print("Not found")

# time complexity --> O(n) --> worst case
# space complexity --> O(1)

# BETTER OPTIMIZED WAY
# lst = [5, 2, 4, 3, 7, 9, 8]
# key = int(input("Enter key: "))
#
# if key in lst:
#     print("Found")
# else:
#     print("Not found")


# WITHOUT USING isFound VARIABLE :
# lst = [5, 2, 4, 3, 7, 9, 8]
# key = int(input("Enter key: "))
#
# for item in lst:
#     if item == key:
#         print("Found")
#         break
# else:
#     print("Not found")