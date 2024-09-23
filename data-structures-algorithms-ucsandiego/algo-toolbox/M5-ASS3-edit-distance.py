"""PROBLEM
5.2.3 Edit Distance
Edit Distance Problem
Compute the edit distance between two strings.
Input: Two strings.
Output: The minimum number of single-symbol insertions, deletions, and substitutions to transform one string into the other one.
"""
def edit_distance_matrix(word1, word2):
    matrix = [[None for letter in word2 + " "] for letter in word1 + " "]

    matrix[0][0] = 0
    for i in range(1, len(word1)+1):
        matrix[i][0] = matrix[i-1][0]+1

    for j in range(1, len(word2)+1):
        matrix[0][j] = matrix[0][j-1]+1

    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            insertion_cost = matrix[i][j-1]+1
            deletion_cost = matrix[i-1][j]+1
            match_or_mismatch_cost = matrix[i-1][j-1] if word1[i-1] == word2[j-1] else matrix[i-1][j-1]+1
            matrix[i][j] = min(insertion_cost, deletion_cost, match_or_mismatch_cost)
    return matrix

def output_alignement(matrix, i, j, alignement, word1, word2):
    if i == j == 0:
        return
    if i >= 0 and matrix[i][j] == matrix[i-1][j] + 1:
        output_alignement(matrix, i-1, j, alignement, word1, word2)
        alignement[0].append(word1[i-1])
        alignement[1].append("-")
    elif j >= 0 and matrix[i][j] == matrix[i][j-1] + 1:
        output_alignement(matrix, i, j-1, alignement, word1, word2)
        alignement[0].append("-")
        alignement[1].append(word2[j-1])
    else:
        output_alignement(matrix, i-1, j-1, alignement, word1, word2)
        alignement[0].append(word1[i-1])
        alignement[1].append(word2[j-1])

word1 = 'editing'
word2 = 'distance'
matrix = edit_distance_matrix(word1, word2)
for row in matrix:
    print(row)

length = len(matrix[0]) - 1 + matrix[len(matrix)-1][len(matrix[0])-1]
alignement = [[], []]

output_alignement(matrix, len(matrix)-1, len(matrix[0])-1, alignement, word1, word2)
for row in alignement:
    print(''.join(row))