"""PROBLEM
6 Pattern matching with mismatches

Problem Introduction
A natural generalization of the pattern matching problem is the following: find all text locations where distance
from pattern is sufficiently small. This problems has applications in text searching (where mismatches
correspond to typos) and bioinformatics (where mismatches correspond to mutations).

Problem Description
Task. For an integer parameter 𝑘 and two strings 𝑡 = 𝑡0𝑡1 · · · 𝑡𝑚−1 and 𝑝 = 𝑝0𝑝1 · · · 𝑝𝑛−1, we say that
𝑝 occurs in 𝑡 at position 𝑖 with at most 𝑘 mismatches if the strings 𝑝 and 𝑡[𝑖 : 𝑖 + 𝑝) = 𝑡𝑖𝑡𝑖+1 · · · 𝑡𝑖+𝑛−1
differ in at most 𝑘 positions.

Input Format. Every line of the input contains an integer 𝑘 and two strings 𝑡 and 𝑝 consisting of lower
case Latin letters.

Constraints. 0 ≤ 𝑘 ≤ 5, 1 ≤ |𝑡| ≤ 200 000, 1 ≤ |𝑝| ≤ min{|𝑡|, 100 000}. The total length of all 𝑡’s does not
exceed 200 000, the total length of all 𝑝’s does not exceed 100 000.

Output Format. For each triple (𝑘, 𝑡, 𝑝), find all positions 0 ≤ 𝑖1 < 𝑖2 < · · · < 𝑖𝑙 < |𝑡| where 𝑝 occurs in 𝑡
with at most 𝑘 mismatches. Output 𝑙 and 𝑖1, 𝑖2, . . . , 𝑖𝑙.

Time Limits. C: 2 sec, C++: 2 sec, Java: 5 sec, Python: 40 sec. C#: 3 sec, Haskell: 4 sec, JavaScript: 10
sec, Ruby: 10 sec, Scala: 10 sec.

Memory Limit. 512MB.
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

def matching_patterns(string, substring, k):
    precomputed_string_m1 = precompute_hashes(string, m1)
    precomputed_string_m2 = precompute_hashes(string, m2)
    precomputed_substring_m1 = precompute_hashes(substring, m1)
    precomputed_substring_m2 = precompute_hashes(substring, m2)
    matching_positions = []

    for index in range(len(string)-len(substring)+1):
        mismatches = 0
        starting_position = 0
        while starting_position < len(substring):
            left = 0
            right = len(substring) - starting_position
            while left<=right:
                length = left + (right-left)//2
                if sub_hash(precomputed_string_m1, m1, index+starting_position, length) == sub_hash(precomputed_substring_m1, m1, starting_position, length):
                    left = length+1
                else:
                    right = length-1
            length = left + (right-left)//2
            if starting_position + length < len(substring):
                mismatches += 1
            starting_position += 1 + length
        if mismatches <= k:
            matching_positions.append(index)
    return [len(matching_positions)] + matching_positions

k, string, substring = input().split()[:3]
k = int(k)
print(' '.join(map(str, matching_patterns(string, substring, k))))