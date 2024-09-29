"""
5.4.5 Coloring a Board
Coloring a Board Problem
Given a positive integer n, find the number of ways to color an n × 3 board by at most four colors in such a way that no two adjacent cells are colored by the same color.
Input: A positive integer n.
Output: The number of ways to color an n × 3 board by at most four colors in such a way that no two adjacent cells are colored by the same color (cells sharing a single point are not considered adjacent).
"""
"""SOLUTION
Solving this problem requires making a leap of understanding the problem by realizing the following nature of the problem:

We can fill the first row and the next either with 2 or 3 colors.
We want to know how many possibilities we have for filling:
First with 2 and second with 2
First with 2 and second with 3
First with 3 and second with 2
First with 3 and second with 3

First with 2 colors: 4*3*1 = 12 options
First with 3 colors: 4*3*2 = 24 options

How many ways can we fill the next row?
If first 2 colors and next 2 colors: 7
If first 2 colors and next 3 colors: 10
If first 3 colors and next 2 colors: 5
If first 3 colors and next 3 colors: 11

Therefore, the second row, for example, would be: 12*(7+10) + 24*(5+11)

The third row would therefore be: 12*(7*(7+10)+10*(5+10)) + 24*(5*(7+10)+11*(5+11))

"""