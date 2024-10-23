"""PROBLEM
3 Merging tables

Problem Introduction
In this problem, your goal is to simulate a sequence of merge operations with tables in a database.

Problem Description
Task. There are 𝑛 tables stored in some database. The tables are numbered from 1 to 𝑛. All tables share
the same set of columns. Each table contains either several rows with real data or a symbolic link to
another table. Initially, all tables contain data, and 𝑖-th table has 𝑟𝑖 rows. You need to perform 𝑚 of
the following operations:
1. Consider table number 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖. Traverse the path of symbolic links to get to the data. That is,
while 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 contains a symbolic link instead of real data do
𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ← symlink(𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖)
2. Consider the table number 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 and traverse the path of symbolic links from it in the same
manner as for 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖.
3. Now, 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 and 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 are the numbers of two tables with real data. If 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ̸=
𝑠𝑜𝑢𝑟𝑐𝑒𝑖, copy all the rows from table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 to table 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖, then clear the table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖
and instead of real data put a symbolic link to 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 into it.
4. Print the maximum size among all 𝑛 tables (recall that size is the number of rows in the table).
If the table contains only a symbolic link, its size is considered to be 0.
See examples and explanations for further clarifications.

Input Format. The first line of the input contains two integers 𝑛 and 𝑚 — the number of tables in the
database and the number of merge queries to perform, respectively.
The second line of the input contains 𝑛 integers 𝑟𝑖 — the number of rows in the 𝑖-th table.
Then follow 𝑚 lines describing merge queries. Each of them contains two integers 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 and
𝑠𝑜𝑢𝑟𝑐𝑒𝑖 — the numbers of the tables to merge.

Constraints. 1 ≤ 𝑛,𝑚 ≤ 100 000; 0 ≤ 𝑟𝑖 ≤ 10 000; 1 ≤ 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖, 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 ≤ 𝑛.

Output Format. For each query print a line containing a single integer — the maximum of the sizes of all
tables (in terms of the number of rows) after the corresponding operation.
"""
"""SOLUTION
In order to solve this problem, we can take advantage of disjoint sets datastructure.

The tables will be represented by a disjoint set.
We add a attribute to the disjoint set data structure that will store the size of each i-th table.
When we merge two tables, we simply set the hanging tree root value to be 0, and we sum its previous value to the the value of the root tree. This should represent the number of lines of the merged trees.

Largest tree on the forest:
We simply keep track of the largest tree on the forest of disjoint sets.
After each merge, we check if resulting table is bigger than max. If so, update max.
"""

class DisjointSet:
    def __init__(self, values):
        self.values = values
        size = len(values)
        self.parent = []
        self.rank = []
        for element in range(size):
            self.parent.append(element)
            self.rank.append(0)
        
    def find_root(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]
        # while self.parent[i] != i:
        #     i = self.parent[i]
        # return i
    
    def merge(self, i, j):
        i -= 1
        j -= 1
        root_of_i = self.find_root(i)
        root_of_j = self.find_root(j)
        if root_of_i == root_of_j:
            return self.values[root_of_i]
        if self.rank[root_of_i] > self.rank[root_of_j]:
            # Set the value (number of rows on the merge) to the root
            self.values[root_of_i] += self.values[root_of_j]
            merged_value = self.values[root_of_i]
            self.values[root_of_j] = 0
            self.parent[root_of_j] = root_of_i
            self.rank[root_of_j] = self.rank[root_of_i]
        elif self.rank[root_of_i] <= self.rank[root_of_j]:
            self.values[root_of_j] += self.values[root_of_i]
            self.values[root_of_i] = 0
            merged_value = self.values[root_of_j]
            self.parent[root_of_i] = root_of_j
            if self.rank[root_of_i] == self.rank[root_of_j]:
                self.rank[root_of_j] += 1
        return merged_value
    
    def __str__(self):
        return str(self.parent)

# n: number of tables
# m: number of merge queries
n, m = map(int, input().split())
rows_per_table = list(map(int, input().split()[:n]))
merge_operations = []
for element in range(m):
    merge_operations.append(list(map(int, input().split())))

tables = DisjointSet(rows_per_table)
max_table = max(rows_per_table)

for operation in merge_operations:
    merged_size = tables.merge(operation[0], operation[1])
    max_table = max(max_table, merged_size)
    print(max_table)