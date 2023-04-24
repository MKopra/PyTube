# METHOD 2 ALL ARRAYS AT ONCE
#class Solution:
 #   def longestCommonPrefix(self, strs: List[str]) -> str:
strs = ['apple', 'ape', 'application']
# create an empty list to store arrays
word_arrays = []

# iterate through each word in the list
for word in strs:
    word_array = []
    # split the word into an array of characters
    for char in word:
        word_array.append(char)
    word_arrays.append(word_array)

# create an empty list to store the common characters
return_list = []

# iterate through the indices of the word arrays
for i in range(len(word_arrays[0])):
    # get the character at the current index in the first word array
    current_char = word_arrays[0][i]
    # assume the current character is common to all strs
    is_common = True
    # iterate through the rest of the word arrays
    for j in range(1, len(word_arrays)):
        # if the current character is different in any of the word arrays
        if word_arrays[j][i] != current_char:
            # mark it as not common
            is_common = False
            break
    # if the current character is common to all word arrays
    if is_common:
        # append it to the list of common characters
        return_list.append(current_char)
    # otherwise, there are no more common characters
    else:
        break

# join the list of common characters into a string
return_string = ''.join(return_list)

# print the longest common prefix
print(return_string)
print(word_arrays[0])

'''
# METHOD 3 SHORTEST WORD
# create a list of strs
strs = ["flower","flow","flight"]

# find the shortest word
shortest_word = min(strs, key=len)

# create an empty list to store arrays
word_arrays = []

# iterate through each word in the list
for word in strs:
    # convert the word to an array of characters
    word_array = list(word)
    # if the word is longer than the shortest word, truncate it
    if len(word_array) > len(shortest_word):
        word_array = word_array[:len(shortest_word)]
    # add the word array to the list
    word_arrays.append(word_array)

# create an empty list to store the common characters
common_chars = []

# iterate through the indices of the word arrays up to the length of the shortest word
for i in range(len(shortest_word)):
    # get the character at the current index in the first word array
    current_char = word_arrays[0][i]
    # assume the current character is common to all strs
    is_common = True
    # iterate through the rest of the word arrays
    for j in range(1, len(word_arrays)):
        # if the current character is different in any of the word arrays
        if word_arrays[j][i] != current_char:
            # mark it as not common
            is_common = False
            break
    # if the current character is common to all word arrays
    if is_common:
        # append it to the list of common characters
        common_chars.append(current_char)
    # otherwise, there are no more common characters
    else:
        break

# join the list of common characters into a string
common_prefix = ''.join(common_chars)

# print the longest common prefix
print(common_prefix)
'''
