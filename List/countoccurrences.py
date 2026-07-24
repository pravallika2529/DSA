# to count occurrences of a ch in a list

lst = [2, 5, 3, 8, 2, 5, 3, 2]
dct = {}

for num in lst:
    if num not in dct:
        dct[num] = 1
    else:
        dct[num] += 1
print(dct)
# similar to counting frequency in string
