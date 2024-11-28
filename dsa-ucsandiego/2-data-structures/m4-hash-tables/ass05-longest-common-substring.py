"""PROBLEM
5 Longest common substring
Problem Introduction
In the longest common substring problem one is given two strings 𝑠 and 𝑡 and the goal is to find a string 𝑤
of maximal length that is a substring of both 𝑠 and 𝑡. This is a natural measure of similarity between two
strings. The problem has applications in text comparison and compression as well as in bioinformatics.
The problem can be seen as a special case of the edit distance problem (where only insertions and
deletions are allowed). Hence, it can be solved in time 𝑂(|𝑠| · |𝑡|) using dynamic programming. Later in
this specialization, we will learn highly non-trivial data structures for solving this problem in linear time
𝑂(|𝑠| + |𝑡|). In this problem, your goal is to use hashing to solve it in almost linear time.

Problem Description

Input Format. Every line of the input contains two strings 𝑠 and 𝑡 consisting of lower case Latin letters.

Constraints. The total length of all 𝑠’s as well as the total length of all 𝑡’s does not exceed 100 000.

Output Format. For each pair of strings 𝑠 and 𝑡𝑖, find its longest common substring and specify it by
outputting three integers: its starting position in 𝑠, its starting position in 𝑡 (both 0-based), and its
length. More formally, output integers 0 ≤ 𝑖 < |𝑠|, 0 ≤ 𝑗 < |𝑡|, and 𝑙 ≥ 0 such that 𝑠𝑖𝑠𝑖+1 · · · 𝑠𝑖+𝑙−1 =
𝑡𝑗 𝑡𝑗+1 · · · 𝑡𝑗+𝑙−1 and 𝑙 is maximal. (As usual, if there are many such triples with maximal 𝑙, output any
of them.)

Time Limits. C: 2 sec, C++: 2 sec, Java: 5 sec, Python: 15 sec. C#: 3 sec, Haskell: 4 sec, JavaScript: 10
sec, Ruby: 10 sec, Scala: 10 sec.
"""
import random

x = random.randint(1, 10**9)
m1 = 10**9 + 7
m2 = 10**9 + 9

def precompute_hashes(string, m):
    hashes = [0]
    current_hash = 0
    for index in range(len(string)):
        current_hash = (current_hash*x + ord(string[index]))%m
        hashes.append(current_hash)
    return hashes

def sub_hash(precomputed_hashes, m, start_index, length):
    sub_hash = (precomputed_hashes[start_index+length] - (x**length)*precomputed_hashes[start_index])%m
    return sub_hash

def longest_common_substring(string1, string2):
    hash_set_m1 = {}
    hash_set_m2 = {}
    
    precomputed_s1_m1 = precompute_hashes(string1, m1)
    precomputed_s1_m2 = precompute_hashes(string1, m2)
    precomputed_s2_m1 = precompute_hashes(string2, m1)
    precomputed_s2_m2 = precompute_hashes(string2, m2)
    longest_common_substring = [-1, -1, 0]

    left = 0
    right = min(len(string1), len(string2))
    while left<=right:
        length = left + (right-left)//2
        for index in range(0, len(string1)-length+1):
            hash_set_m1[sub_hash(precomputed_s1_m1, m1, index, length)] = index
            hash_set_m2[sub_hash(precomputed_s1_m2, m2, index, length)] = index
        for index in range(0, len(string2)-length+1):
            if sub_hash(precomputed_s2_m1, m1, index, length) in hash_set_m1 and sub_hash(precomputed_s2_m2, m2, index, length) in hash_set_m2:
                longest_common_substring = [hash_set_m1[sub_hash(precomputed_s2_m1, m1, index, length)], index, length]
        if longest_common_substring[2] == length:
            left = length+1
        else:
            right = length-1
        hash_set_m1 = {}
        hash_set_m2 = {}
    length = left + (right-left)//2
    return longest_common_substring

string1, string2 = input().split()[:2]
print(' '.join(map(str, longest_common_substring(string1, string2))))