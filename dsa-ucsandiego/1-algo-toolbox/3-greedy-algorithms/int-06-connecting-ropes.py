"""
Connect Ropes with Minimal Cost Problem
Find the minimum cost of connecting n ropes into one where the cost of connecting two ropes is the sum of their lengths.
Input: An array of distinct integers where each integer represents the length of a rope. 
The cost to connect two ropes is equal to the sum of their lengths.
Output: A minimum-cost way to connect all ropes into a single one.
"""

"""
SOLUTION
End result is an array [a, b, c, d, e], where the sum of pairwise sums is minimal a+b + b+c + c+d + d+e = a + 2b + 2c + 2d + e

To minimize this sum, the only important thing is that the two largest ropes are on the edges: a and e.
This way, the largest values are not multiplied by two. Only the remaining values which are lower.

To prove this, suppose there is an array where a < c which is optimized.
The cost of this array is
a + 2b + 2c + 2d + e

If we permute a with c, we should get a higher sum, because it would not be optimized, so:

c + a >= 2c

Since a < c, it is impossible that c + a > c + can
So it is proven that a and e should be the largest ropes on the list.

To produce the result we expect then, we sort the array on reverse order, than we pop the first element and append it to the array
"""

def minimal_cost_ropes(ropes):
    ropes.sort(reverse=True)
    ropes.append(ropes.pop(0))
    return ropes

print(minimal_cost_ropes([1, 2, 3, 4, 5]))