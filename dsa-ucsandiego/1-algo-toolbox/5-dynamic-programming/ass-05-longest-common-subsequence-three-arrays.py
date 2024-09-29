"""
5.2.5 Longest Common Subsequence of Three Sequences
Longest Common Subsequence of Three Sequences Problem
Compute the maximum length of a common subsequence of three sequences.
Input: Three sequences.
Output: The maximum length of a common subsequence

Input format. First line: n. 
Second line: a1 ,a2 ,...,an. 
Third line: m. 
Fourth line: b1 ,b2 ,...,bm. 
Fifth line: l. Sixth line: c1 , c2 ,..., cl.
Output format. p.
Constraints. 1 ≤ n,m,l ≤ 100; −10**9 ≤ ai ,bi, ci ≤ 10**9.
"""
def longest_common_subsequence(seq1, seq2, seq3):
    matrix = [[[None for element in seq3 + [0]] for element in seq2 + [0]] for element in seq1 + [0]]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j][0] = 0

    for i in range(len(matrix)):
        for k in range(len(matrix[0][0])):
            matrix[i][0][k] = 0

    for j in range(len(matrix[0])):
        for k in range(len(matrix[0][0])):
            matrix[0][j][k] = 0 

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            for k in range(1, len(matrix[0][0])):
                matrix[i][j][k] = max(
                    matrix[i-1][j-1][k-1] + 1 if seq1[i-1] == seq2[j-1] == seq3[k-1] else matrix[i-1][j-1][k-1],
                    matrix[i-1][j-1][k],
                    matrix[i-1][j][k-1],
                    matrix[i][j-1][k-1],
                    matrix[i-1][j][k],
                    matrix[i][j-1][k],
                    matrix[i][j][k-1]
                )
    return matrix[i][j][k]

n = int(input())
seq1 = [int(element) for element in input().split()[:n]]
m = int(input())
seq2 = [int(element) for element in input().split()[:m]]
l = int(input())
seq3 = [int(element) for element in input().split()[:l]]
print(longest_common_subsequence(seq1, seq2, seq3))