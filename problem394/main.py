# This problem was asked by Uber.

# Given a binary tree and an integer k, return whether there exists a root-to-leaf path that sums up to k.

# For example, given k = 18 and the following binary tree:

#     8
#    / \
#   4   13
#  / \   \
# 2   6   19
# Return True since the path 8 -> 4 -> 6 sums to 18.

## Solution ## 

# Like all binary tree problems, we must think recursively to find a root-to-leaf path. 
# Assume we already have a function path_exists(). 
# Then, we know if a path exists for our current problem if either node.left or node.right can make k - node.val, since we can just add node.val to it to make a path from the leaf to the current node.

# Let's formalize this line of thinking. First, let's consider the base cases:
# 1) If the node is null, return False as there's no way to make k. 
# 2) If we are on a leaf node, then return whether the current node's value is k.
# Then the recursive step:
# 3) If we are not on a leaf node, then return True if either node.left OR node.right can make k - node.val.


class Node:
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_exists(node, k):
    if node is None:
        return False
    
    if node.left is None and node.right is None:
        return node.val == k
    path_exists(node.left, k - node.val) or path_exists(node.right, k - node.val)
