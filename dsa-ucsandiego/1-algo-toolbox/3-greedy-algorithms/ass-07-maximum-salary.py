"""
Largest Concatenate Problem
Compile the largest integer by concatenating the given integers.
Input: A sequence of positive integers.
Output: The largest integer that can be obtained by concatenating the given integers in some order.
"""

def better_than2(n1, n2):
    for i in range(min(len(n1), len(n2))):
        if n1[i] > n2[i]:
            return True
        elif n1[i] < n2[i]:
            return False
        else:
            pass
    print("N1, N2:", n1, n2, len(n1), len(n2))
    if n1 == '891': print("Aqui:", n1[len(n2)], n2[-1])
    if len(n1) < len(n2):
        if n2[len(n1)] > n1[-1]:
            return False
        if n2[len(n1)] < n1[-1]:
            return True
    elif len(n1) > len(n2):
        if n1[len(n2)] > n2[-1]:
            return True
        if n1[len(n2)] < n2[-1]:
            return False
    elif len(n1) == len(n2):
        return True

def better_than(n1, n2):
    if int(n1+n2) >= int(n2+n1):
        return True
    else:
        return False

def largest_concatenate(n, list):
    if len(list) <= 1:
        return list

    pivot = list[0]
    better_than_pivot = []
    worse_than_pivot = []
    for index, element in enumerate(list[1:]):
        if better_than(element, pivot):
            better_than_pivot.append(element)
        else:
            worse_than_pivot.append(element)
    return largest_concatenate(len(better_than_pivot), better_than_pivot) + [pivot] + largest_concatenate(len(worse_than_pivot), worse_than_pivot)

n = int(input())
salaries = [element for element in input().split()]
print(''.join(largest_concatenate(n, salaries)))
# print(largest_concatenate(5, ['8', '86', '891', '866', '89']))
