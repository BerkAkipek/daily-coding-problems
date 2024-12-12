# This problem was asked by Google.

# Given a string, return the length of the longest palindromic subsequence in the string.

# For example, given the following string:

# MAPTPTMTPA
# Return 7, since the longest palindromic subsequence in the string is APTMTPA. 
# Recall that a subsequence of a string does not have to be contiguous!

# Your algorithm should run in O(n^2) time and space.

## Solution ## 

# The brute force method to solve this problem would be to generate every possible subsequence and test whether it's a palindrome:

def is_palindrome(s):
    return s == s[::-1]


def generate_subsequences(s):
    if s == '':
        return ['']
    
    result = []
    rest = generate_subsequences(s[1:])
    result.extend(rest)
    result.extend(s[0] + subseq for subseq in rest)
    return result


def longest_palindromic_subsequence_naive(s):
    longest = ''
    for subsequence in generate_subsequences(s):
        if is_palindrome(subsequence) and len(subsequence) > len(longest):
            longest = subsequence
    return longest

# However, this takes exponential time -- O(2^N), so we should find a better way.

# Notice that we are doing a lot of repeated computations here. 
# We can use dynamic programming to store the results of these computations. Here's how.

# 1) Create a 2D, N by N matrix. 
# Each entry at matrix[i][j] will represent the longest palindromic subsequence in the string from index i to j 
# 2) Initialize the matrix by setting each value at matrix[i][i] to the character at s[i], since every character is a one-length palindrome. 
# 3) Fill in the rest of the matrix with the following rule:
# - If `s[i] == s[j]`, then we can make a larger palindromic subsequence by taking the largest one we have from `i + 1` to `i - 1` and prepending / appending the character.
# - Otherwise, fallback to the longest subsequence we can make from either `i + 1` to `j` or `i` to `j - 1`.
# 4) Return the result at matrix[0][len(s) - 1], since that's the longest palindromic subsequence of the entire string.

def longest_palindromic_subsequence(s):
    matrix = [['' for _ in range(len(s))] for _ in range(len(s))]

    for i, char in enumerate(s):
        matrix[i][i] = char
    
    for i in reversed(range(len(s))):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                matrix[i][j] = s[i] + matrix[i+1][j-1] + s[j]
            else:
                matrix[i][j] = max(matrix[i+1][j], matrix[i][j-1], key=lambda s: len(s))
    
    return matrix[0][len(s) - 1]

# Since we're now only doing a doubly-nested for loop over s, this algorithm now only takes O(n^2) time and space.
