"""PROBLEM
5.4.3 Interleaving Strings
Interleaving Strings Problem
Given strings A, B, and C, output an interleaving of A and B that is equal to C or “−1” if such an interleaving does not exist.
Input: Strings A, B, and C.
Output: Interleaving of A and B that is equal to C or “−1” if such an interleaving does not exist. 
Interleaving of A and B is a string of length |A| + |B| that has symbols of A (in order) interleaved with symbols of B (in order).
"""
"""SOLUTION
The interleaving exists if we match A to C and B to C, and on all position that AC have insertions, AD has deletions.
"""

def edit_distance_matrix(str1, str2):
    matrix = [[0 for element in str2 + ' '] for element in str1 + ' ']
    matrix[0][0] = 0
    for i in range(1, len(matrix)):
        matrix[i][0] = matrix[i-1][0] + 1
    for j in range(1, len(matrix[0])):
        matrix[0][j] = matrix[0][j-1] + 1

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] = min(
                matrix[i-1][j-1] if str1[i-1] == str2[j-1] else float('inf'),
                matrix[i-1][j-1] + 1 if str1[i-1] == str2[j-1] else float('inf'),
                matrix[i-1][j] + 1,
                matrix[i][j-1] + 1
            )
    return matrix

def modified_string(str1, str2, matrix) -> str:
    i = len(matrix)-1
    j = len(matrix[0])-1

    output1 = []
    output2 = []

    while i > 0 or j > 0:
        if matrix[i][j] == matrix[i-1][j-1] + 1:
            output1.append(str1[i-1])
            output2.append(str2[j-1])
            i -= 1
            j -= 1
        elif matrix[i][j] == matrix[i][j-1] + 1:
            output1.append('-')
            output2.append(str2[j-1])
            j -= 1
        elif matrix[i][j] == matrix[i-1][j] + 1:
            output1.append(str1[i-1])
            output2.append('-')
            i -= 1
        elif matrix[i][j] == matrix[i-1][j-1]:
            output1.append(str1[i-1])
            output2.append(str2[j-1])
            i -= 1
            j -= 1
    output1.reverse()
    output2.reverse()
    return output1, output2


def interleaving(str1, str2, str3):
    matrix1 = edit_distance_matrix(str1, str3)
    matrix2 = edit_distance_matrix(str2, str3)
    modified_str1 = ''.join(modified_string(str1, str3, matrix1)[0])
    modified_str2 = ''.join(modified_string(str2, str3, matrix2)[0])

    result = True
    for i, letter in enumerate(str1):
        if not (modified_str1[i] == '-' or modified_str2[i] == '-') and modified_str1[i] != modified_str2[i]:
            result = False
    return result

str1 = 'tree'
str2 = 'sort'
str3 = 'tsroerte'

print(interleaving(str1, str2, str3))