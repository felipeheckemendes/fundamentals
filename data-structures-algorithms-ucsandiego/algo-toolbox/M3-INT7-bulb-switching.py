"""
Bulb Switching Problem
Given a binary vector representing an initial state of n bulbs connected by wires into a linear sequence, find the minimum number of switches to press for turning on all bulbs.
Each bulb has a switch that changes the state of this bulb and all bulbs to the right of it.

Input: A binary vector representing an initial state of n bulbs connected by wires into a single linear sequence. 0’s and 1’s in this array corresponds to the turnedoff and turned-on bulbs, respectively. 
Each bulb has a switch that changes the state of this bulb and all bulbs to the right of it. 
In other words, the i-th switch changes a vector x1 ,..., xi−1 , xi , xi+1,..., xn into a vector x1 ,..., xi−1 ,1 − xi ,1 − xi+1,...,1 − xn.

Output: The length of an optimal switch-series, i.e., the minimum number of switches to press for turning on all bulbs
"""
"""
SOLUTION

[1, 0, 0, 1, 0, 1]

Switch the first 0
[1, 1, 1, 0, 1, 0]
[1, 1, 1, 1, 0, 1]
[1, 1, 1, 1, 1, 0]
[1, 1, 1, 1, 1, 1]

Switch the last 0
[1, 0, 0, 1, 1, 0]
[1, 0, 0, 1, 1, 1]
[1, 1, 1, 0, 0, 0]
[1, 1, 1, 1, 1, 1]

Both switch the first and last result in the same result. However, switching first is easier to implement.
furthermore, we do not need to switch the array every time to get the minimum. All we need to do is count how many times the number changes, basically.

Switch the middle
[1, 0, 1, 0, 1, 0]
[1, 0, 1, 1, 0, 1]
[1, 1, 0, 0, 1, 0]
[1, 1, 0, 1, 0, 1]
[1, 1, 1, 0, 1, 0]
[1, 1, 1, 1, 0, 1]
[1, 1, 1, 1, 1, 0]
[1, 1, 1, 1, 1, 1]
"""

def minimum_switches(bulbs):
    num_switches = 0
    criteria = 0
    for bulb in bulbs:
        if bulb == criteria:
            num_switches += 1
            criteria = abs(criteria-1)
    return num_switches

print(minimum_switches([1, 0, 0, 1, 0, 1, 1, 0, 0, 0]))