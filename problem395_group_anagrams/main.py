# This problem was asked by Robinhood.

# Given an array of strings, group anagrams together.

# For example, given the following array:

# ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
# Return:

# [['eat', 'ate', 'tea'],
#  ['apt', 'pat'],
#  ['now']]

## Solution ## 

# If we sort all words lexicographically, all anagrams will have the same sorted order. 
# So, one solution would be to keep a dictionary where the key is the sorted word and the value is the list of words that map to it. 
# We can use Python's defaultdict library to easily create this type of mapping:

from collections import defaultdict


def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)

    result = []
    for group in groups.values():
        result.append(group)
    return result
