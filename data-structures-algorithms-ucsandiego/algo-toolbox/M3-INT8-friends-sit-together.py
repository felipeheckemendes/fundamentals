"""
Friends Seat Together Problem
Given positions of k friends in the first row of a theater, find the minimal number of moves to sit all friends together.
In each move, a friend moves to a seat to the left or a seat to the right.

Input: A set of k distinct positive integers in the interval from 1 to N. 
This set represents positions of k friends that have bought individual (not necessarily adjacent) seats in the first row of a theater.
Since all other seats in the first row turned out to be empty, the friends want to start moving to the neighboring seats (to the left or to the right)
 and continue until they all sit together in k consecutive chairs.

Output: Find the minimal number of moves to sit all friends together.

"""
"""
SOLUTION

Lets explore some examples

3 People
[1, 4, 7]

I think we should choose 1 person to remain still, so that such person minimizes its movements.
If we choose first person, the other 2 will need to move 4-1 + 7-1 = 9
If we choose the middle person, the other 2 will need to move 4-1 + 7-4 = 6
If we choose the last, the other 2 will need to move 7-4 + 7-1 = 9
From this we infer that it is best for the person on the middle to remain still, this way minimizing the distance from the others

4 Peoople

[1, 4, 6, 10]
Similarly, we should choose someone to stay sill, and move the people around it closer.
Lets choose the second person
First round total moves = 4-1 + 6-4 = 5
Second roung total moves = 10-5 = 5
Total moves = 10

Lets choose the third person now and see the difference
First round = 6-4 + 10-6 = 6
Second round = 5-1 = 4
Total moves = 10

Both seem ideally equal.

5 People
[1, 4, 6, 9, 14]
Choose the middle person
6-4 + 9-6 + 5-1 + 14-7 = 16

Choose the second person
4-1 + 6-4 + 9-5 + 14-6 = 17

Choose the first person
4-1 + 6-2 + 9-3 + 14-4 = 23

Choose the third person
14-9 + 9-6 + 8-4 + 7-1 = 18

6 People

[1, 4, 6, 9, 11, 20]

6-4 + 5-1 + 9-6 + 11-7 + 20-8 = 25

11-9 + 20-10 + 9-6 + 8-4 + 7-1 = 25

THE MEDIAN IS THE GREEDY CHOICE
"""

def minimum_moves(seating_positions):
    # Select the median
    median_index = len(seating_positions)//2
    median = seating_positions[median_index]
    # Compute number of people between item and median
    people_between = []
    for index, people in enumerate(seating_positions):
        people_between.append(abs(median_index - index) - 1)
    print(people_between)

    # Calculate minimum seating positions
    moves = 0
    for index, person in enumerate(seating_positions):
        if person != median:
            moves += abs(median - person) - people_between[index]

    return moves

print(minimum_moves([1, 4, 6, 9, 14]))