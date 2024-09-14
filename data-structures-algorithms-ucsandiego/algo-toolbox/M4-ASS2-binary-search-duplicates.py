"""
4.2.2 Binary Search with Duplicates
Donald Knuth, the author of The Art of Computer Programming, famously
said: “Although the basic idea of binary search is comparatively straightforward, the details can be surprisingly tricky.” He was referring to a modified
classical Binary Search Problem:

Binary Search with Duplicates Problem
Find the index of the first occurrence of a key in a sorted array.
Input: A sorted array of integers (possibly with duplicates) and an integer q.
Output: Index of the first occurrence of q in the array or “−1” if q does not appear in the array

Input format. The first two lines of the input contain an integer n and a sequence k0 ≤ k1 ≤ ··· ≤ kn−1 of n positive integers in non-decreasing order.
The next two lines contain an integer m and m positive integers q0 ,q1 ,...,qm−1

Output format. For all i from 0 to m − 1, output the index 0 ≤ j ≤ n − 1 of the first occurrence of qi (i.e., kj = qi ) or −1, if there is no such index.
Constraints. 1 ≤ n ≤ 3 · 10**4; 1 ≤ m ≤ 10**5 ; 1 ≤ ki ≤ 10**9 for all 0 ≤ i < n; 1 ≤ qj ≤ 10**9 for all 0 ≤ j < m.
"""

def binary_search(arr, search):
    left, right = 0, len(arr) - 1
    while left<right:
        mid = left + (right-left)//2
        if arr[mid] < search:
            left = mid + 1
        elif arr[mid] >= search:
            right = mid
    return right if arr[right] == search else -1

n = int(input())
arr = [int(element) for element in input().split()[:n]]
m = int(input())
search_arr = [int(element) for element in input().split()[:m]]
print(" ".join(map(str, [binary_search(arr, search_element) for search_element in search_arr])))