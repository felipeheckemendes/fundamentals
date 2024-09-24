"""
5.2.4 Longest Common Subsequence of Two Sequences
Longest Common Subsequence of Two Sequences Problem
Compute the maximum length of a common subsequence of two sequences.
Input: Two sequences.
Output: The maximum length of a common subsequence.

Input format. First line: n. 
Second line: a1 ,a2 ,...,an. 
Third line: m. 
Fourth line: b1 ,b2 ,...,bm.
Output format. p.
"""
def longest_common_subsequence(seq1, seq2):
    matrix = [[None for element in seq2 + [0]] for element in seq1 + [0]]
    for submatrix in matrix:
        submatrix[0] = 0
    for j in range(len(matrix[0])):
        matrix[0][j] = 0

    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            subsequence_insert = matrix[i-1][j]
            subsequence_delete = matrix[i][j-1]
            subsequence_match = matrix[i-1][j-1] + 1 if seq1[i-1] == seq2[j-1] else matrix[i-1][j-1]
            matrix[i][j] = max(subsequence_insert, subsequence_delete, subsequence_match)
    return matrix[i][j]

n = int(input())
seq1 = [int(element) for element in input().split()]
m = int(input())
seq2 = [int(element) for element in input().split()]
print(longest_common_subsequence(seq1, seq2))