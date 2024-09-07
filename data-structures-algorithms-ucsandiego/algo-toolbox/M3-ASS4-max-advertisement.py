"""
Maximum Product of Two Sequences Problem
Find the maximum dot product of two sequences
of numbers
"""

# The greedy approach easily provable is that the maximum sum of products combines the largest items of one list with the largest of the other list.
# Assuming both lists are the same length, we can just sort them and then multiply.

def max_revenue(clicks, prices):
    clicks.sort()
    prices.sort()
    revenue = 0
    for index in range(len(clicks)):
        revenue += clicks[index]*prices[index]
    return revenue

items = int(input())
clicks = [int(element) for element in input().split()]
prices = [int(element) for element in input().split()]
print(max_revenue(clicks, prices))

