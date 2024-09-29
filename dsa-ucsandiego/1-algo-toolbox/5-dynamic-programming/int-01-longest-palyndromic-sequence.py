"""PROBLEM
5.4.1 Longest Palindromic Subsequence
Longest Palindromic Subsequence Problem
Given a string, find a longest palindromic subsequence of this string, i.e., a subsequence that reads the same backward and forward.
Input: A string.
Output: A longest palindromic subsequence of this string, i.e., a subsequence that reads the same backward and forward (this subsequence does not have to be contiguous).
"""
"""SOLUTION
If we take two letters in index i and j of the given string, the size of the largest palindromic sequence starting and ending on these two letters is:
if string[i] == string[j] -> 2 + longest palindromic sequence on the string from i+1 to j-1
if string[i] != string[j] -> the longest palindromic sequence in either i to j-1 or i+1 to j.
We build a table matirx[i, j] to store the size of the longest palindromic sequence from index i to j on the string.
The longest on the given string will be the value on matrix[0, len(string)-1]
"""
def longest_palindrome(string):
    matrix = [[0 for element in string] for element in string]
    string = [letter for letter in string]
    n = len(string)

    for i in range(n):
        matrix[i][i] = 1
    
    for dif in range(1, n):
        for i in range(0, n - dif):
            j = i + dif
            if string[i] == string[j]:
                matrix[i][j] = matrix[i+1][j-1] + 2
            else:
                matrix[i][j] = max(matrix[i+1][j-1], matrix[i+1][j])

    return matrix, matrix[0][n-1]
    
result = longest_palindrome('axbyczbsak')
for element in result[0]:
    print(element)
print(result[1])

