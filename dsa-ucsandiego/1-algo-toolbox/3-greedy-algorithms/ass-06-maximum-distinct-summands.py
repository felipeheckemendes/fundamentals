"""
Distinct Summands Problem
Represent a positive integer as the sum of the
maximum number of pairwise distinct positive
integers.

Input: A positive integer n.
Output: The maximum k such
that n can be represented as the
sum a1 + ··· + ak of k distinct positive integers.

You are organizing a competition for children and have n candies to give as prizes. 
You would like to use these candies for top k places in this competition with a restriction that a higher place gets a larger number of candies.
To make as many children happy as possible, you need to find the largest value of k for which it is possible.
"""

def maximum_summands(n):
    
    sum = 0
    summands = []

    for number in range(1, n+1):
        # print(sum, number, n)
        if sum + number > n:
            summands[-1] = summands[-1] + n - sum
            sum = n
        else:
            sum += number
            summands.append(number)
    return summands
        

n = int(input())
result = maximum_summands(n)
print(len(result))
print(" ".join(map(str, result)))



