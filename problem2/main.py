# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def products(lst):
    pr = 1
    for i in range(len(lst)):
        pr *= lst[i]
    result = []
    for j in range(len(lst)):
        result.append(pr // lst[j])
    return result

# This is approach with division runs in O(N) time.

print(products([1, 2, 3, 4, 5]))

# Without division, another approach would be to first see that the ith element simply needs the product of numbers before i and the product of numbers after i. 
# Then we could multiply those two numbers to get our desired product.

# In order to find the product of numbers before i, we can generate a list of prefix products. 
# Specifically, the ith element in the list would be a product of all numbers including i. 
# Similarly, we would generate the list of suffix products.

def products(lst):
    prefix_products = []
    for num in lst:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)
    
    suffix_products = []
    for num in reversed(lst):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    result = []
    for i in range(len(lst)):
        if i == 0:
            result.append(suffix_products[i+1])
        elif i == len(lst) - 1:
            result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1] * suffix_products[i+1])
    return result

print(products([1, 2, 3, 4, 5]))

# This runs in O(N) time and space, since iterating over the input arrays takes O(N) time and creating the prefix and suffix arrays take up O(N) space.