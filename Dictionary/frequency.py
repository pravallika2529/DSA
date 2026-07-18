# count the word frequency using a dictionary

string = "i love python programming learning python is fun"
words = string.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word count: ", word_count)

# time complexity --> to split, and then the loop --> O(n) + O(n) = O(n)
# space complexity --> O(n) --> because words list is stored up to n words

# now, for more efficient storage, we don't have to store in a list,
# word_count = {}
#
# for word in string.split():
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1