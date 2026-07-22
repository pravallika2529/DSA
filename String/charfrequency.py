# count character frequency in a string

string = input("Enter a string: ")
dct = {}

for ch in string:
    if ch != " ":
        if ch not in dct:
            dct[ch] = 1
        else:
            dct[ch] += 1
print(dct)

# ANOTHER WAY --> IMP --> GET METHOD
# string = input("Enter a string: ")
# dct = {}
#
# for ch in string:
#     if ch != " ":
#         dct[ch] = dct.get(ch, 0) + 1
#
# print(dct)

# dct.get(...) --> this is get method, used to get values of keys
# dct.get(ch, 0) + 1 --> '0' is the default value
# '0' means the ch is not yet in dictionary, and we increment 1 to this