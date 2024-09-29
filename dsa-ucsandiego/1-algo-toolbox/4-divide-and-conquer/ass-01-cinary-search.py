"""
Sorted Array Multiple Search Problem
Search multiple keys in a sorted sequence of keys.
Input: A sorted array K of distinct integers and an array Q = [q0 ,...,qm−1] of integers.
Output: For each qi, check whether it occurs in K.

Input format. The first two lines of the input contain an integer n and a sequence k0 < k1 < ... < kn−1 of n distinct positive integers in increasing order. 
The next two lines contain an integer m and m positive integers q0,q1,...,qm−1

Output format. For all i from 0 to m−1, output an index 0 ≤ j ≤ n−1 such that kj = qi, or −1, if there is no such index.

Constraints. 
1 ≤ n ≤ 3 · 10**4; 
1 ≤ m ≤ 10**5; 
1 ≤ ki ≤ 10**9
for all 0 ≤ i < n;
1 ≤ qj ≤ 10**9
for all 0 ≤ j < m.
"""
def binary_search(arr, search_element):
    left, right = 0, len(arr) - 1
    while left<right:
        mid = (left+right)//2
        if arr[mid] == search_element:
            return mid
        elif arr[mid] < search_element:
            left = mid + 1
        elif arr[mid] > search_element:
            right = mid - 1
    return -1

n = int(input())
arr = [int(element) for element in input().split()[:n]]
m = int(input())
search_arr = [int(element) for element in input().split()[:m]]
print(" ".join(map(str, [binary_search(arr, search_element) for search_element in search_arr])))