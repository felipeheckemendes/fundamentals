"""PROBLEM STATEMENT
Points and Segments Problem
Given a set of points and a set of segments on a line, compute, for each point, the number of segments it is contained in.
Input: A list of segments and a list of points.
Output: The number of segments containing each point.

You are organizing an online lottery. To participate, a person bets on a single integer. 
You then draw several segments of consecutive integers at random. A participant’s payoff is proportional to the number of segments that contain the participant’s number. 
You need an efficient algorithm for computing the payoffs for all participants.
A simple scan of the list of all ranges for each participant is too slow since your lottery is very popular: you have thousands of participants and thousands of ranges.

Input format. The first line contains two non-negative integers n and m defining the number of segments and the number of points on a line, respectively. 
The next n lines contain two integers li, ri defining the i-th segment [li, ri]. 
The next line contains m integers defining points p1,..., pm.

Output format. m non-negative integers k1,...,kp where ki is the number of segments that contain pi.

Constraints. 1 ≤ n,m ≤ 50000; −10**8 ≤ li ≤ ri ≤ 10**8 for all 1 ≤ i ≤ n;−10**8 ≤ pj ≤ 10**8 for all 1 ≤ j ≤ m.
"""
"""SOLUTION
We will use a divide and conquer approach.
1st: Sort both points and segments (sort segments by starting point, then by ending point *** VERY IMPORTANT TO SORT BY ENDING POINT ALSO)
Divide and conquer approach:
2nd: For each point, we check on a reduced list of segments if they are contained. This list is represented by first_active_index and current_segment_index
    We go through all segments that start before the first point
    For each segment that start before, and ends at or after the point, we increase the counter
    If the segment ends before the point, we remove it from the list of lookup segments (incrementing first_active_index)
    We store the counter for that element

    For the next points:
    We go through the list of selected segments and see if any of them end before the new point. If so, we reduce the counter, and advance the first_active_index

"""

def quick_sort(arr, lower, upper):
    if upper <= lower:
        return arr

    m1, m2, i = lower, upper, lower+1
    while m2 >= i:
        # print(arr, m2, i)
        if arr[i][1] < arr[m1][1]:
            arr[i], arr[m1] = arr[m1], arr[i]
            m1 += 1
            i += 1
        elif arr[i][1] > arr[m1][1]:
            arr[i], arr[m2] = arr[m2], arr[i]
            m2 -= 1
        elif arr[i][1] == arr[m1][1]:
            i += 1
    quick_sort(arr, lower, m1-1)
    quick_sort(arr, m2+1, upper)
    return arr

def quick_sort_segments(arr, lower, upper, criteria):
    """
    arr -> array to be sorted in place
    lower -> lower bound inclusive of section to sort
    upper -> upper bound inclusive of section to sort
    criteria -> 0 if sorting by starting point, then by ending point
                1 if sorting only by ending point
    """
    if upper <= lower:
        return arr
    
    m1, m2, i = lower, upper, lower+1

    while m2 >= i:
        # print(arr, m2, i)
        if arr[i][1][criteria] < arr[m1][1][criteria]:
            arr[i], arr[m1] = arr[m1], arr[i]
            m1 += 1
            i += 1
        elif arr[i][1][criteria] > arr[m1][1][criteria]:
            arr[i], arr[m2] = arr[m2], arr[i]
            m2 -= 1
        elif arr[i][1][criteria] == arr[m1][1][criteria]:
            i += 1
        
    if criteria == 0:
        quick_sort_segments(arr, m1, m2, 1)
    quick_sort_segments(arr, lower, m1-1, criteria)
    quick_sort_segments(arr, m2+1, upper, criteria)
    return arr

def number_intersections(points: list[int], segments: list[tuple[int, int]]) -> list[int]:
    pivot = points[0]
    points = list(enumerate(points))
    points = quick_sort(points, 0, len(points)-1)
    segments = list(enumerate(segments))
    segments = quick_sort_segments(segments, 0, len(segments)-1, 0)
    result = [None for element in points]
    counter = 0
    current_segment_index = 0
    first_active_index = 0

    for point in points:
        for index in range(first_active_index, current_segment_index):
            if segments[index][1][1] < point[1]:
                counter -= 1
                first_active_index += 1
            if segments[index][1][1] >= point[1]:
                break
        while current_segment_index < len(segments) and segments[current_segment_index][1][0] <= point[1]:
            if segments[current_segment_index][1][1] >= point[1]:
                counter += 1
            current_segment_index += 1
        result[point[0]] = counter
    return result

segments = []
m, n = [int(element) for element in input().split()]
for i in range(m):
    segment = input().split()
    segment = [int(segment[0]), int(segment[1])]
    segments.append(segment)
points = [int(point) for point in input().split()[:n]]
result = number_intersections(points, segments)

# For quicker testing without all inputs, use below:
# result = number_intersections([5, 4, 3, 2, 1, 0], [[1, 3], [2, 4], [4,5], [3, 6], [3, 5], [3, 4], [0, 1]])

print(" ".join(map(str, result)))
