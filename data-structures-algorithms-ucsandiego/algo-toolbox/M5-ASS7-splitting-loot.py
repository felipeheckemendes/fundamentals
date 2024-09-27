"""
5.2.7 Splitting the Pirate Loot
3-Partition Problem
Partition a set of integers into three subsets with equal sums.
Input: A sequence of integers v1, v2,..., vn.
Output: Check whether it is possible to partition them into three subsets with equal sums, i.e., check whether there exist three disjoint sets 
S1, S2, S3 ⊆ {1,2,...,n}
such that S1∪S2∪S3 = {1,2,...,n}
and Σ|i∈S1 (vi) = Σ|j∈S2 (vj) = Σ|k∈S3 (vk).

Input format. The first line contains an integer n. 
The second line contains integers v1, v2,..., vn separated by spaces.
Output format. Output 1, if it possible to partition v1, v2,..., vn into three subsets with equal sums, and 0 otherwise.
Constraints. 1 ≤ n ≤ 20, 1 ≤ vi ≤ 30 for all i.
"""
"""SOLUTION
The solution using dynamic programming is as follows:
Let TOTAL be the sum of all elements in the set. Check if it is divisible by 3. If not, set is not 3-way partitionable.
For a set to be partitionable in 3 equal subsets, there must exist 2 subsets with subtotal = TOTAL/3
SUBPROBLEMS
We want to check wether with the first j elements on the set, we can build two subsets of total sum h and i.
We assign matrix[h][i][j] 1 if we can build the two subsets and 0 if not possible.

In the case where j=len(subset), h=TOTAL/3 and i=TOTAL/3, we would be checking wether we can take two partitions both of which have a third of TOTAL, therefore checking if it is 3-way partitionable.
To get to this case, we build a dynamic programming table and build up to it.

The recurrence relation for building is as follows:
1st: if it is possible to build two subsets with subtotals h and i using j-1 elements, using j elements would also be possible
2nd:             if it is possible to build two subsets with subtotals h - element(j) and i using j-1 elements, then it is also possible to build two subsets with subtotals h and i using j elements
3rd: conversely, if it is possible to build two subsets with subtotals h and i - element(j) using j-1 elements, then it is also possible to build two subsets with subtotals h and i using j elements

The base cases are:
1st: It is possible to build subsets with subtotals h=0 and i=0 with any j elements.
2nd a: It is possible to build subsets with subtotal h and i=0 with the first j=0 element, only when element(0) == h
2nd b: It is possible to build subsets with subtotal h=0 and i with the first j=0 element, only when element(0) == i

"""
def build_dynamic_programming_table(S, sum):
    matrix = [[[0 for element in range(len(S))] for element in range(sum+1)] for element in range(sum+1)]
    
    for j in range(len(matrix[0][0])):
        matrix[0][0][j] = 1

    for h in range(1, len(matrix)):
        if S[0] == h:
            matrix[h][0][0] = 1

    for i in range(1, len(matrix[0])):
        if S[0] == i:
            matrix[0][i][0] = 1

    for h in range(len(matrix)):
        for j in range(1, len(matrix[0][0])):
            if matrix[h][0][j-1] == 1 or (h-S[j] >= 0 and matrix[h-S[j]][0][j-1] == 1):
                matrix[h][0][j] = 1
    for i in range(len(matrix[0])):
        for j in range(1, len(matrix[0][0])):
            if matrix[0][i][j-1] == 1 or (i-S[j] >= 0 and matrix[0][i-S[j]][j-1] == 1):
                matrix[0][i][j] = 1

    for h in range(1, len(matrix)):
        for i in range(1, len(matrix[0])):
            for j in range(1, len(matrix[0][0])):
                if matrix[h][i][j-1] == 1 or (h-S[j] >= 0 and matrix[h-S[j]][i][j-1] == 1) or (i-S[j] >= 0 and matrix[h][i-S[j]][j-1] == 1):
                    matrix[h][i][j] = 1

    return matrix

def three_way_partitionable(numbers):
    summation = 0
    for element in numbers:
        summation += element
    if summation % 3 != 0:
        return 0
    subset_summation = summation//3
    matrix = build_dynamic_programming_table(numbers, subset_summation)

    """# Printing the matrix (for visualization)
    for i, layer in enumerate(matrix[0]):
        print("\nLayer i", i, "=")
        for h, row in enumerate(matrix):
            # print(row)
            for j, element in enumerate(matrix[h][i]):
                print(f" {element} ", end= "|")
            print("")
    """

    # Checking if partitionable
    if matrix[len(matrix)-1][len(matrix[0])-1][len(matrix[0][0])-1] == 1:
        return 1
    else:
        return 0

# Sample sets for testing
# numbers = [2, 3, 4, 5, 5, 7, 10, 25, 19, 12, 8, 7, 1]
# numbers = [1, 3, 7, 37, 2, 4, 5, 7, 4, 2, 5, 12, 19]
# numbers = [1, 3, 2, 2, 3, 1]
# Standart input according to assignement specification:
n = int(input())
numbers = list(map(int, input().split()[:n]))

print(three_way_partitionable(numbers))
"""
WRONG SOLUTION BELOW
This wrong solution is the following:
0 - Check if the sum is divisible by 3. If so, do steps below:
1 - Take a knapsack of capacity SUM/3
2 - Remove the items taken on this knapsack from the list
3 - Take another knapasck of capacity SUM/3
4 - If it is successful in taking the two knpsacks, the remaining items' sum should also be SUM/3, therefore the set is partitionable in 3 equal subsets

The problem with this approach is that there may be more than 3 subsets whose subtotal are SUM/3.
Some of these subsets might result in the remaining subset not being partitionable.
If the first knapsack happens to take such a subset, the second knapsack will return False. However, there might another subset that could be taken on the first knapsack that would result in optimal partitioning.

def partitionable_in_three(arr):
    
    def backtracking(i, j):
        if i < 0 or j < 0:
            return
        # print("Check", i, j, matrix[i][j], matrix[i-1][j-arr[i-1]] + arr[i-1])
        # print("Before", items_taken, i, j, arr)
        # print(matrix[i][j], matrix[i-1][j-arr[i-1]] + arr[i-1])
        if matrix[i][j] == matrix[i-1][j-arr[i-1]] + arr[i-1]:
            items_taken.append(arr[i-1])
            # print("After", items_taken)
            backtracking(i-1, j-arr[i-1])
        else:
            # print("After2", items_taken)
            backtracking(i-1, j)
    
    
    sum = 0
    for element in arr:
        sum += element
    if sum % 3 != 0:
        return 0
    else:
        capacity = int(sum/3)
    # print(capacity)
    
    # First loot
    matrix = [[0 for element in range(capacity+1)] for element in arr]
    for i in range(1, len(matrix)):
        for w in range(1, len(matrix[0])):
            matrix[i][w] = matrix[i-1][w]
            if w-arr[i-1] >=0:
                weight = matrix[i-1][w-arr[i-1]] + arr[i-1]
                if weight >= matrix[i][w]:
                    matrix[i][w] = weight
        
    items_taken = []
    backtracking(len(matrix)-1, len(matrix[0])-1)
    print("items =", items_taken)
    # print('items taken 1', items_taken)
    for item in items_taken:
        arr.remove(item)
    # print('remaining 1', arr)
    if matrix[len(matrix)-1][len(matrix[0])-1] != capacity:
        print("Returned 1st")
        return False

    # Second loot
    matrix = [[0 for element in range(capacity+1)] for element in arr]
    for i in range(1, len(matrix)):
        for w in range(1, len(matrix[0])):
            matrix[i][w] = matrix[i-1][w]
            if w-arr[i-1] >=0:
                weight = matrix[i-1][w-arr[i-1]] + arr[i-1]
                if weight >= matrix[i][w]:
                    matrix[i][w] = weight
        
    items_taken = []
    backtracking(len(matrix)-1, len(matrix[0])-1)
    print("items =", items_taken)
    # print('items taken 2', items_taken)
    for item in items_taken:
        arr.remove(item)
    # print('remaining 2', arr)
    if matrix[len(matrix)-1][len(matrix[0])-1] != capacity:
        print("Returned 2nd")
        return False

    # Third loot
    matrix = [[0 for element in range(capacity+1)] for element in arr]
    for i in range(1, len(matrix)):
        for w in range(1, len(matrix[0])):
            matrix[i][w] = matrix[i-1][w]
            if w-arr[i-1] >=0:
                weight = matrix[i-1][w-arr[i-1]] + arr[i-1]
                if weight >= matrix[i][w]:
                    matrix[i][w] = weight
        
    items_taken = []
    backtracking(len(matrix)-1, len(matrix[0])-1)
    print("items =", items_taken)
    # print("items taken 3", items_taken)
    for item in items_taken:
        arr.remove(item)
    # print("remaining 3", arr)
    if matrix[len(matrix)-1][len(matrix[0])-1] != capacity or len(arr)>0:
        print("Returned 3rd")
        return False
    
    return True


# matrix = partitionable_in_three([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25])
partitionable = partitionable_in_three([25, 19, 12, 10, 8, 7, 7, 5, 5, 4, 3, 2, 1])
print(partitionable)
# for element in matrix:
#     print(element)

