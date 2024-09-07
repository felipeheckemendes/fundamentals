"""
Covering Segments by Points Problem
Find the minimum number of points needed to cover all given segments on a line.
Input: A sequence of n segments [l1, r1],...,[ln, rn] on a line.
Output: A set of points of minimum size such that each segment [li, ri] contains a point, i.e., 
there exists a point x from this set such that li ≤ x ≤ ri.

You are responsible for collecting signatures from all tenants in a building. For each tenant, you know a period of time when he or she is at home.
You would like to collect all signatures by visiting the building as few times
as possible. For simplicity, we assume that when you enter the building,
you instantly collect the signatures of all tenants that are in the building at
that time.
"""

def visits(ranges):
    # Do a greedy approach.

    # Initialization of starts and ends lists
    starts = [range[0] for range in ranges]
    ends = [range[1] for range in ranges]
    visits = 0
    intersecting_indexes = []
    chosen_points = []

    # Check all lines intersecting. 
    while len(ranges) > 0:

        # Set first point to be the leftmost point with a line
        current_point = min(starts)
    # Advance and intersect new lines, but if any of the intesecting lines reaches its end, stop.
        # Check if there any other intersections currently
        for index, element in enumerate(ranges):
            if element[0] <= current_point <= element[1]:
                intersecting_indexes.append(index)
        
        stop = False
        while stop == False:
            # Advance 1 position
            current_point += 1
            # Add new intersections
            for index, element in enumerate(ranges):
                if element[0] <= current_point <= element[1] and index not in intersecting_indexes:
                    intersecting_indexes.append(index)
            # Check if any of the intersections have reached its end. If yes, continue. If not, advance once more
            for intersecting in intersecting_indexes:
                # print(intersecting, intersecting_indexes, current_point)
                if ends[intersecting] == current_point:
                    chosen_points.append(current_point)
                    stop = True
        
        # Select this endpoint as first point.
            # Trivially done on current_point
        # Count one more visit
        visits += 1
        
        # Remove all intersecting lines from the list
        new_ranges = []
        new_starts = []
        new_ends = []
        for index, element in enumerate(ranges):
            if index not in intersecting_indexes:
                new_ranges.append(element)
                new_starts.append(element[0])
                new_ends.append(element[1])
        ranges = new_ranges
        starts = new_starts
        ends = new_ends
        intersecting_indexes = []
        # Repeat problem for remaining list
    
    return [visits, chosen_points]

print(visits([[1, 3], [2, 5], [3, 6]]))