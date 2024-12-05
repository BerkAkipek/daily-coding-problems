# This problem was asked by Airbnb.

# Given an array of integers, return the largest range, inclusive, of integers that are all included in the array.

# For example, given the array [9, 6, 1, 3, 8, 10, 12, 11], return (8, 12) since 8, 9, 10, 11, and 12 are all in the array.

## Solution ##

# One straightforward way to find the longest consecutive range might be to sort the array and then find all consecutive ranges by looking at adjacent elements. 
# However, sorting our numbers would take O(n log n). 
# Can we think of a faster way?

# If we hash all the numbers or add them to a set, then we can quickly look up adjacent numbers in constant time. 

# So, one solution would be the following:
# 1) Add all numbers to a dictionary or set (O(n) time) 
# 2) Iterate through each number, check whether it's the start of a range by checking for num - 1 in the set 
# 3) If it is the start of a range, then keep incrementing a temp variable and checking for it in our set 
# 4) Once we've reached the end of the current range we're processing, check whether it's the largest we've seen so far.

def largest_consecutive_range(arr):
    nums = set(arr)
    longest_range = (0, 0)
    for num in nums:
        if num - 1 not in nums:
            curr = num + 1
            while curr in nums:
                curr += 1
            if curr - num > longest_range[1] - longest_range[0]:
                longest_range = (num, curr -1)
    return longest_range

# This runs in O(n) time, since we iterate one entire loop over nums.
