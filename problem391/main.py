# This problem was asked by Facebook.

# We have some historical clickstream data gathered from our site anonymously using cookies. 
# The histories contain URLs that users have visited in chronological order.

# Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appear in both.

# For example, given the following two users' histories:

# user1 = ['/home', '/register', '/login', '/user', '/one', '/two']
# user2 = ['/home', '/red', '/login', '/user', '/one', '/pink']
# You should return the following:

# ['/login', '/user', '/one']

## Solution ## 

# The naive approach here would be to check all contiguous sequences from user1 and user2, keeping track of the longest identical one. 
# One way to accomplish this would be to generate all possible subarrays of one of the users, and then check if that exact subarray exists anywhere in the other user.

def longest_contiguous_history(user1, user2):
    longest_result = []
    for i in range(len(user1)):
        for j in range(i + 1, len(user1) + 1):
            subarray1 = user1[i:j]
            for k in range(len(user2) - len(subarray1)):
                subarray2 = user2[k:k + len(subarray1)]
                if subarray1 == subarray2 and len(subarray1) > len(longest_result):
                    longest_result = subarray1
    return longest_result


# However, this would be inefficient: O(N^2 M L), where N is the length of user1, M the length of user2, and L the longest # of characters of a URL. 
# We can speed this up slightly by comparing clickstream lengths and selecting the smaller of the two to perform the double nested for loop on, but instead, we should use dynamic programming to find the longest contiguous common subarray.

# The algorithm is similar to finding the longest common substring of two strings. 
# We'll use the following invariant: in a 2D (N + 1) * (M + 1) matrix, the value at (i, j) will contain the longest matching subarray up to i and j for each respective array.

# More specifically:
# 1) First, we'll initialize a 2D matrix of size N + 1 * M + 1. 
# 2) Go over the 0th row and column, and initialize them to the empty list (this is our base case) 
# 3) Iterate over the rest of the matrix, and execute the following algorithm:

# - If user1[i] is equal to user2[j], set the value to `matrix[i - 1][j - 1] + user1[i]`
# - Otherwise, set the value in the matrix at (i, j) to `[]`
# Then, we simply need to return the longest value we've seen so far.

import numpy as np


def longest_contiguous_history(user1, user2):
    matrix = [[None for _ in range(len(user2) + 1)] for _ in range(len(user1) + 1)]

    for i in range(len(user1) + 1):
        matrix[i][0] = []

    for j in range(len(user2) + 1):
        matrix[0][j] = []
    # Populate the matrix with longest common subarrays between histories
    for i in range(1, len(user1) + 1):
        for j in range(1, len(user2) + 1):
            if user1[i - 1] == user2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + [user1[i - 1]]
            else:
                matrix[i][j] = []
    # Go ahead and find the longest contiguous common subarray
    longest_result = []
    for i in range(len(user1) + 1):
        for j in range(len(user2) + 1):
            if len(matrix[i][j]) > len(longest_result):
                longest_result = matrix[i][j]
    return longest_result

# Now this only takes O(N M L) time, since we use dynamic programming to build our matrix from the bottom-up.


def main():
    user1 = ['/home', '/register', '/login', '/user', '/one', '/two']
    user2 = ['/home', '/red', '/login', '/user', '/one', '/pink']
    print(longest_contiguous_history(user1=user1, user2=user2))


if __name__ == '__main__':
    main()
