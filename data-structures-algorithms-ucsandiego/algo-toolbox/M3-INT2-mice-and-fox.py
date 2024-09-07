"""
Mice and a Fox Problem
Given positions of n mice and n holes on a line, find an optimal hiding strategy for mice.

Input: Integer arrays m(1),...,m(n) and h(1),..., h(n) that represent positions of mice and holes on a line. 
Mice noticed a fox and they all are trying to escape into holes in minimum time. 
All mice move with the same speed and each hole can hold only a single mouse. 
You can assume that mice are superintelligent, know where the holes are, and care about each other.
Output: A permutation (i1 ,..., in) such that
    max(k=1,...,n) |m(k) − h(ik)|
is minimized over all possible permutations. 
Here, ik represents the hole where the k-th mice will eventually hide in.

"""


# My intuition tells me that sorting both lists gives us the hole on which each mouse should go.
# This choses for each mouse the nearest possible hole to him.
