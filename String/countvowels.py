# counting the no. of vowels in a string

string = input("Enter a string: ")
count = 0
for ch in string:
    if ch in 'aeiou' or ch in 'AEIOU':
        count = count + 1

print("The no. of vowels is: ", count)