# This problem was asked by Two Sigma.

# You are given an unsorted list of 999,000 unique integers, each from 1 and 1,000,000. 
# Find the missing 1000 numbers. What is the computational and space complexity of your solution?

## Solution ##

# I can sort the list then find the numbers with a O(N logN) time

def find_missing_numbers(lst):
    result = []
    sort = sorted(lst)      # O(N logN)
    for i in range(1, 1000000):
        if i != sort[i]:
            result.append(i)
            sort.insert(i+1, 0)     # O(N)
    return result

# Yes this algorithm has O(N * logN) time.

# Now let's try the O(N) option:

def find_missing_numbers(lst):
    referance, result = [], []
    for i in range(1,1000000):
        referance.append(0)
    for element in lst:
        referance[element] = element
    for i in range(len(referance)):   
        if referance[i] == 0:
            result.append(i)
    return result

# This algorithm has O(N) time and space

# If there was only one missing integer, we could sum up all the numbers and subtract n * (n + 1) / 2 by it, which should give us the missing number. 
# However, in this case, we have multiple missing numbers, so we can't know from the result which numbers in particular are missing.

# Instead, we can create a bitarray of length 1,000,000 and add all the numbers in our list to a set. 
# Then, we iterate through numbers 1 to 1,000,000 and mark the bitarray at position i if we found it in the set.

# Finally, we perform a sort of roll call and check each bit at position i from 1 to 1,000,000 and if it's not set, then add it to our list of results.

def find_missing_numbers(lst):
    bitarray = [False for _ in range(1000000)]
    s = set(lst)
    for i in range(1, 100001):
        if i in s:
            bitarray[i-1] = True
    result = []
    for i in range(1, 1000001):
        if not bitarray[i-1]:
            result.append(i)
    return result

# Now this only takes O(n) time, since set addition and existence checks are O(1). 
# If we're dealing strictly with the constant 1,000,000, you could argue that it's constant time. 
# In addition, to calculate the space usage, it would essentially be 1,000,000 bits, or 125,000 bytes, or 125 kilobytes of space.
