"""PROBLEM
4.3.4 Unbounded Binary Search
Unbounded Binary Search Problem
Given a monotonically increasing function f (x) on positive integers, find the value of x where f (x) = 0 (or report that none exists).
Input: A monotonically increasing function f (x) on positive integers (given as a black box) that takes both negative and nonnegative values.
Output: Value of x where f (x) = 0 or “−1” if such value does not exist.
"""
"""SOLUTION
The key realization for solving this is the way we find new pivots.
Since we are unbounded above, we can just double the number of elements we skip on each loop while going up
If we reach a point which is higher than 0, switch to normal binary search between previou lookup and current lookup indexes.
"""
def binary_search(function, lower, upper):
    while lower < upper:
        mid = lower + (upper - lower)//2
        if function(mid) < 0:
            lower = mid + 1
        elif function(mid) >= 0:
            upper = mid
    if function(upper) == 0:
        return upper
    else:
        return -1

def binary_search_unbound(function):
    if function(0) == 0:
        return 0
    
    lookup = 1
    while not (function(lookup) <= 0 and function(lookup+1) >= 0):
        if function(lookup) < 0:
            lookup = lookup*2
        if function(lookup) > 0:
            return binary_search(function, lookup//2, lookup)
    if function(lookup) == 0:
        return lookup
    elif function(lookup+1) == 0:
        return lookup + 1
    else:
        return -1

def function(n):
    return n - 10

print(binary_search_unbound(function))
