# This problem was asked by Amazon.

# Given a linked list and an integer k, remove the k-th node from the end of the list and return the head of the list.

# k is guaranteed to be smaller than the length of the list.

# Do this in one pass.

## Solution ##

# Without the one-pass restriction, we could calculate the length of the entire list with a pointer and a counter, and then restart from the beginning, go n - k steps, and remove the node at that spot.

# However, since we're limited to to only one pass, we have to think more creatively. 
# One common trick frequently used in linked list problems is concept of fast and slow pointers. 
# In this case, we can have two pointers, one moving k steps ahead of the other one (the slow one). 
# Then, when the fast one reaches the end of the linked list, we know that the slow pointer is k steps from the end, and we can remove it there.

class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt


def print_ll(head):
    s = ''
    curr = head
    while curr is not None:
        s += str(curr.val)
        S += '->'
        curr = curr.nxt
    print(s)


def remove_kth_node_from_end(head, k):
    fast = head
    for i in range(k):
        fast = fast.nxt
    
    slow = head
    while fast.nxt is not None:
        fast = fast.nxt
        slow = slow.next
    
    slow.nxt = slow.nxt.nxt

# This algorithm takes O(N) as it only does one pass with two pointers.