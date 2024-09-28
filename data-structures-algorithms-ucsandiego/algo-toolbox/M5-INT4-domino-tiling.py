"""
5.4.4 Domino Tiling
Domino Tiling Problem
Given a positive integer n, find the number of ways to fill an n × 3 board by 2 × 1 dominos.
Input: A positive integer n.
Output: The number of ways to fill an n×3 board by 2×1 dominos.
"""
"""SOLUTION
0  : Realize that tiles with odd n don't fill completely, but can at most have 1 tile uncovered.
1st: Realize that a 3 x 2 tile has 3 different ways of filling

2nd: The key insight is that we need to look at odd states (in which there are tile gaps) in order to built a recurrence relation.

3nd: Let A be the number of tilings that complete (0 for odds)
     Let B be the number of tilings that have 1 tile missing (0 for evens)

Then:
B(n) = 2*A(n-1) + B(n-2)
A(n) = A(n-2) + B(n-1)

The reasoning for both recurrences is:
To build A(n): 
    We can start at B(n-1), and for each B(n-1), there is only one way to insert the new 2 blocks. In this case we have B(n-1) possibilities.
    Also, there is one way that We can from A(n-2) and fill it without passing through any state of B(n-1). (That is, by putting three blocks on the same direction). In this case we have A(n-2) possibilities.
    So A(n) = B(n-1) + A(n-2)

TO build B(n):
    We can start at A(n-1),and for each B(n-1), there are two ways to insert the new block. In this case we have 2*A(n-1) possibilities.
    Also, there is one way that We can start at B(n-2) and fill it without passing through any state of (A-1). (That is, by putting two blocks on the same direction). In this case we have B(n-2) possibilities.
    So B(n) = 2*A(n-1) + B(n-2)
"""
def number_domino_tilings(n):
    A = [0]*(n+1)
    B = [0]*(n+1)
    A[0] = 1

    for i in range(1, n+1):
        if i % 2 == 0:
            A[i] =  B[i-1] + A[i-2]
        else:
            B[i] = 2*A[i-1] + B[i-2]
    return A[n]

print(number_domino_tilings(8))
        
""" O(n**2) solution
def domino_tiling(n):
    matrix = [0 for _ in range(n+1)]

    matrix[0] = 1
    matrix[1] = 0
    matrix[2] = 3
    
    for i in range(3, n+1):
        if i % 2 == 0:
            for j in range(0, i):
                matrix[i] += 2*matrix[j]
            matrix[i] += matrix[i-2]
    return matrix
print(domino_tiling(10))
"""