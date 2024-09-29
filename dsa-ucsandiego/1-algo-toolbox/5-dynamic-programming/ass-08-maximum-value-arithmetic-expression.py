"""PROBLEM
5.2.8 Maximum Value of an Arithmetic Expression
Maximum Value of an Arithmetic Expression Problem
Parenthesize an arithmetic expression to maximize its value.
Input: An arithmetic expression consisting of digits as well as plus, minus, and multiplication signs.
Output: Add parentheses to the expression in order to maximize its value.

Input format. The only line of the input contains a string s of length 2n + 1 for some n, with symbols s0, s1,..., s2n. 
Each symbol at an even position of s is a digit (that is, an integer from 0 to 9) while each symbol at an odd position is one of three operations from {+,-,*}.
"""
"""SOLUTION
1st: Break the expression/subexpression i-j at operator at all index k between i and j-1.
2nd: We need both the minimum (m) and maximum (M) value resulting from the two subexpressions to left and right of every k.
3rd: We take the max of all possibilities of operating left and right with k operator.

MAX = -infinity
MIN = infinity
For every k:
    MAX = max of:
                  > MAX
                  > M(i,k) operator_k M(k+1, j) 
                  > m(i,k) operator_k M(k+1, j) 
                  > M(i,k) operator_k m(k+1, j) 
                  > m(i,k) operator_k m(k+1, j)
    MIN = min  of:
                  > MIN
                  > M(i,k) operator_k M(k+1, j) 
                  > m(i,k) operator_k M(k+1, j) 
                  > M(i,k) operator_k m(k+1, j) 
                  > m(i,k) operator_k m(k+1, j)

M(i, j) = MAX
m(i,j) = MIN

4th: Base case:
    When i = j, both M(i,j) and m(i,j) are equal to value(i)

5th: M(0,n) is the answer to the problem
We build up to this M(0, n) using a dynamic programming table, instead of a recurrence.
"""

def max_and_min(i, j, maxs, mins, operators):
    current_max = float('-inf')
    current_min = float('inf')

    for k in range(i, j):
        if operators[k] == '+':
            current_max = max(current_max, maxs[i][k] + maxs[k+1][j])
            current_min = min(current_min, mins[i][k] + mins[k+1][j])
        if operators[k] == '-':
            current_max = max(current_max, maxs[i][k] - mins[k+1][j])
            current_min = min(current_min, mins[i][k] - maxs[k+1][j])
        if operators[k] == '*':
            current_max = max(
                current_max,
                maxs[i][k] * maxs[k+1][j],
                maxs[i][k] * mins[k+1][j],
                mins[i][k] * maxs[k+1][j],
                mins[i][k] * mins[k+1][j],
            )
            current_min = min(
                current_min,
                maxs[i][k] * maxs[k+1][j],
                maxs[i][k] * mins[k+1][j],
                mins[i][k] * maxs[k+1][j],
                mins[i][k] * mins[k+1][j],
            )
    return current_max, current_min

def maximum_value_expression(expression):
    values = [int(expression[i]) for i, _ in enumerate(expression) if i % 2 == 0]
    operators = [expression[i] for i, _ in enumerate(expression) if i % 2 == 1]
    n = len(values)

    maxs = [[0 for element in values] for element in values]
    mins = [[0 for element in values] for element in values]

    # Base case
    for i in range(n):
        maxs[i][i] = values[i]
        mins[i][i] = values[i]

    # Filling the table on order of increasing j-i (from 1 to n)
    for dif in range(1, n):
        for i in range (0, n - dif):
            j = i + dif
            maxs[i][j], mins[i][j] = max_and_min(i, j, maxs, mins, operators)

    return maxs[0][n-1]

# Sample inputs for testing
# result = maximum_value_expression('1+2+3+4+5')
# result = maximum_value_expression('1-2-3-4-5')
# result = maximum_value_expression('5-8+7*4-8+9')

# Standart input according to assignement specification:
expression = input()
result = maximum_value_expression(expression)
# Standart output according to assingment specification:
print(result)