# to count the no. of digits in a given string

string = input("Enter a string: ")
count = 0
for ch in string:
    if ord(ch) >= 48 and ord(ch) <= 57:
        count += 1

print("The no. of digits in the string is: ", count)