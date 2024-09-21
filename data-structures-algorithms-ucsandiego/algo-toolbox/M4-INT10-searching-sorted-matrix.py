"""
4.3.10 Searching a Sorted Matrix
Searching a Sorted Matrix Problem
Given a sorted n×n integer matrix (i.e., a matrix where each row and each column is sorted in the increasing order) and an integer q, output the position of q in this matrix or “−1” if q does not appear in the matrix.
Input: A sorted n × n integer matrix (i.e., a matrix where each row and each column is sorted in the increasing order) and an integer q.
Output: The position of q in this matrix or “−1” if q does not appear in the matrix.
"""
"""SOLUTION
Solution 1: Do a binary search for each line, this would result O(n*logn) time

Solution 2: Start at the top right element.
If this element is smaller than target, all elements on the row also are: discard current row and move to next
If this element is greater than target, all elements on the column also are: discard current column and move to next
"""
def search_matrix(matrix, target):
    i = 0
    j = len(matrix) - 1
    while i >= 0 and j >=0:
        if matrix[i][j] < target:
            i += 1
        elif matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] == target:
            return i, j
    return -1, -1


matrix = [
    [ 1,  3,  4,  7, 13, 20, 27],
    [ 6, 13, 14, 21, 27, 34, 40],
    [10, 19, 21, 26, 31, 36, 42],
    [17, 25, 29, 36, 38, 40, 45],
    [20, 30, 37, 40, 45, 51, 56],
    [23, 36, 43, 49, 50, 56, 57],
    [26, 39, 47, 56, 58, 63, 69],
]
print(search_matrix(matrix, 36))