"""
5.2.2 Primitive Calculator
Primitive Calculator Problem
Find the minimum number of operations needed to get a positive integer n from 1 by using only three operations: add 1, multiply by 2, and multiply by 3.
Input: An integer n.
Output: The minimum number of operations “+1”, “×2”, and “×3” needed to get n from 1.

Input format. An integer n.
Output format. In the first line, output the minimum number k of operations needed to get n from 1. 
In the second line, output a sequence of intermediate numbers. 
That is, the second line should contain positive integers a0 ,a1 ,...,ak such that a0 = 1, ak = n and for all 1 ≤ i ≤ k, ai is equal to either ai−1 + 1, 2ai−1, or 3ai−1. 
If there are many such sequences, output any one of them.
"""
def minimum_operations(target):
    num_operations = [0, 0]
    for number in range(2, target+1):
        add_one_cost = num_operations[number-1] + 1
        multiply_two_cost = num_operations[int(number/2)] + 1 if number % 2 == 0 else float('inf')
        multiply_three_cost = num_operations[int(number/3)] + 1 if number % 3 == 0 else float('inf')
        num_operations.append(min(add_one_cost, multiply_two_cost, multiply_three_cost))
    return num_operations

def output_sequence(num_operations, number):
    if num_operations[number-1] == num_operations[number] - 1:
        output_sequence(num_operations, number - 1)
        print(number-1, end=" ")
    elif number % 2 == 0 and num_operations[int(number/2)] == num_operations[number] - 1:
        output_sequence(num_operations, int(number/2))
        print(int(number/2), end=" ")
    elif number % 3 == 0 and num_operations[int(number/3)] == num_operations[number] - 1:
        output_sequence(num_operations, int(number/3))
        print(int(number/3), end=" ")

number = int(input())
num_operations = minimum_operations(number)
print(num_operations[number])
output_sequence(num_operations, number)
print(number)