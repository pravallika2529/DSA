# to find the average of numbers in a list

lst = [2, 3, 5, 1, 8, 6, 9]
avg = 0
for num in lst:
    avg = avg + num
avg = avg / len(lst)

print("The average is: ", avg)

# time complexity --> O(n)
# space complexity --> O(1)
# we can also use the sum(lst) method to find sum