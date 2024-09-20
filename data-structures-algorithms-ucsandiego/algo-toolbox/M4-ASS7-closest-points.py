"""
4.2.7 Closest Points
Closest Points Problem
Find the closest pair of points in a set of points on a plane.
Input: A list of n points on a plane.
Output: The minimum distance between a pair of these points.
"""
"""SOLUTION
 We first sort the given n points
by their x-coordinates and then split the resulting sorted list into two halves S1 and S2 of size n2. 
By making a recursive call for each of the sets S1 and S2, we find the minimum distances d1 and d2 in them. 
Let d = min{d1, d2}. 
However, we are not done yet as we also need to find the minimum distance between points from different sets (i.e, a point from S1 and a point from S2) and check whether it is smaller than d. 
To perform such a check, we filter the initial point set and keep only those points whose x-distance to the middle line does not exceed d. 
Afterward, we sort the set of points in the resulting strip by their y-coordinates and scan the resulting list of points. 
For each point, we compute its distance to the seven subsequent points in this list and compute d′, the minimum distance that we encountered during this scan. 
Afterward, we return min{d, d′}.
"""

import math
def quick_sort_x(points, lower, upper):
    if upper - lower <= 0:
        return

    m1, m2, i = lower, upper, lower+1
    while i <= m2:
        if points[i][0] < points[m1][0]:
            points[i], points[m1] = points[m1], points[i]
            m1 += 1
            i +=1
        elif points[i][0] == points[m1][0]:
            i += 1
        elif points[i][0] > points[m1][0]:
            points[i], points[m2] = points[m2], points[i]
            m2 -= 1
    
    quick_sort_x(points, lower, m1-1)
    quick_sort_x(points, m2+1, upper)
    return points

def quick_sort_y(points, lower, upper):
    if upper - lower <= 0:
        return

    m1, m2, i = lower, upper, lower+1
    while i <= m2:
        if points[i][1] < points[m1][1]:
            points[i], points[m1] = points[m1], points[i]
            m1 += 1
            i +=1
        elif points[i][1] == points[m1][1]:
            i += 1
        elif points[i][1] > points[m1][1]:
            points[i], points[m2] = points[m2], points[i]
            m2 -= 1
    
    quick_sort_y(points, lower, m1-1)
    quick_sort_y(points, m2+1, upper)


def binary_search_lowerx(points, value):
    
    lower, upper = 0, len(points) - 1
    while lower < upper:
        mid = lower + (upper-lower)//2
        if points[mid][0] < value:
            lower = mid+1
        elif points[mid][0] >= value:
            upper = mid
    return upper

def binary_search_upperx(points, value):
    
    lower, upper = 0, len(points) - 1
    while lower < upper:
        mid = lower + (upper-lower+1)//2
        if points[mid][0] <= value:
            lower = mid
        elif points[mid][0] > value:
            upper = mid-1
    return upper

def closest_points(points, lower, upper, points_y):
    if upper - lower == 1:
        return math.sqrt( (points[upper][0]-points[lower][0])**2 + (points[upper][1]-points[lower][1])**2 )
    if upper - lower <= 0:
        return float('inf')
    

    # Recursively call the function on the left and right regions
    partition_line = points[(upper-lower)//2][0] # = 5 - 2 // 2 = 3//2 = 1
    d1 = closest_points(points, lower, lower+(upper-lower)//2, points_y) # = 2, 3
    d2 = closest_points(points, lower+(upper-lower)//2+1, upper, points_y) # = 2, 5

    # Set d as the minimum of d1 and d2
    d = min(d1, d2)

    # Find the strip of points less than d distance from partition line
    # strip = points[binary_search_lowerx(points, partition_line - d) : binary_search_upperx(points, partition_line + d)]
    strip = [element for element in points_y if (partition_line - d) <= element[1] <= (partition_line + d) ]

    # Check whether any two points on the strip between line - d and line + d have distance smaller than d. Set d as minimum of d' and d
    if len(strip) >= 2:
        quick_sort_y(strip, 0, len(strip)-1)
        for index, point in enumerate(strip):
            for i in range(index+1, min(7, len(strip)-index)):
                distance = math.sqrt( (strip[index][0]-strip[i][0])**2 + (strip[index][1]-strip[i][1])**2 )
                if distance < d:
                    d = distance
    return d

# Below is hardcoded input for testing:
# points_x = [[4, 4], [-2, -2], [-3, -4], [-1, 3], [2, 3], [-4, 0], [1, 1], [-1, -1], [3, -1], [-4, 2], [-2, 4]]
# points_y = [element for element in points_x]
# quick_sort_x(points_x, 0, len(points_x)-1)
# quick_sort_y(points_y, 0, len(points_y)-1)
# print(closest_points(points_x, 0, len(points_x)-1, points_y))

# Below is std input according to asignment specification
n = int(input())
points_x = []
for i in range(n):
    points.append([int(element) for element in input().split()])
points_y = [element for element in points_x]
quick_sort_x(points_x, 0, len(points)-1, points_y)
print(closest_points(points, 0, n))
