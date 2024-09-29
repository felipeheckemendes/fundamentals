"""PROBLEM
5.4.2 Longest Repeating Subsequence
Longest Repeating Subsequence Problem
Given a string, find a longest repeating subsequence of this string.
Input: A string.
Output: A longest repeating subsequence of this string.
"""
"""SOLUTION
This problem is very similar to the longest common subsequence. 
Particularities: 
1 - we utilise the same string to compare with itself 
2 - and we don't allow matching on diagonals
"""
def lcs(string):
    matrix = [[0 for element in string + '-'] for element in string + '-']

    for i, _ in enumerate(matrix):
        matrix[i][0] = 0
    for j, _ in enumerate(matrix[0]):
        matrix[0][j] = 0
    
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)):
            matrix[i][j] = max(
                matrix[i-1][j-1] + 1 if i != j and string[i-1] == string[j-1] else float('-inf'),
                matrix[i-1][j],
                matrix[i][j-1],
            )
    return matrix


string = 'acacbbeb'
matrix = lcs(string)

print("     ", end="")
for element in string:
    print(f"{element:>2} ", end="")
print("")
for i, row in enumerate(matrix):
    if i > 0:
        print(string[i-1], row)
    else:
        print(" ", row)

print(matrix[len(matrix)-1][len(matrix[0])-1])