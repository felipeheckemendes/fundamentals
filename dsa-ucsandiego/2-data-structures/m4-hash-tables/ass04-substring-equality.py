"""PROBLEM
4 Substring equality
Problem Introduction
In this problem, you will use hashing to design an algorithm that is able to preprocess a given string 𝑠
to answer any query of the form “are these two substrings of 𝑠 equal?” efficiently. This, in turn, is a basic
building block in many string processing algorithms.

Problem Description

Input Format. The first line contains a string 𝑠 consisting of small Latin letters. The second line contains
the number of queries 𝑞. Each of the next 𝑞 lines specifies a query by three integers 𝑎, 𝑏, and 𝑙.

Constraints. 1 ≤ |𝑠| ≤ 500 000. 1 ≤ 𝑞 ≤ 100 000. 0 ≤ 𝑎, 𝑏 ≤ |𝑠| − 𝑙 (hence the indices 𝑎 and 𝑏 are 0-based).

Output Format. For each query, output “Yes” if 𝑠𝑎𝑠𝑎+1. . .𝑠𝑎+𝑙−1 = 𝑠𝑏𝑠𝑏+1. . .𝑠𝑏+𝑙−1 are equal, and “No” otherwise.

Time Limits. C: 1 sec, C++: 1 sec, Java: 2 sec, Python: 10 sec. C#: 1.5 sec, Haskell: 2 sec, JavaScript: 5 sec, Ruby: 5 sec, Scala: 5 sec.
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

outputs = []
string = input()
n_queries = int(input())
precomputed_hashes_m1 = precompute_hashes(string, m1)
precomputed_hashes_m2 = precompute_hashes(string, m2)
for _ in range(n_queries):
    start1, start2, length = map(int, input().split()[:3])
    if sub_hash(precomputed_hashes_m1, m1, start1, length) == sub_hash(precomputed_hashes_m1, m1, start2, length) and \
       sub_hash(precomputed_hashes_m2, m2, start1, length) == sub_hash(precomputed_hashes_m2, m2, start2, length):
        outputs.append("Yes")
    else:
        outputs.append("No")
for element in outputs:
    print(element)