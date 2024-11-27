"""PROBLEM
Problem Introduction
In this problem, your goal is to implement the Rabin–Karp’s algorithm.

Problem Description
Task. In this problem your goal is to implement the Rabin–Karp’s algorithm for searching the given pattern
in the given text.

Input Format. There are two strings in the input: the pattern 𝑃 and the text 𝑇.

Constraints. 1 ≤ |𝑃| ≤ |𝑇| ≤ 5 · 10**5. The total length of all occurrences of 𝑃 in 𝑇 doesn’t exceed 108. The
pattern and the text contain only latin letters.
Output Format. Print all the positions of the occurrences of 𝑃 in 𝑇 in the ascending order. Use 0-based
indexing of positions in the the text 𝑇.
Time Limits. C: 1 sec, C++: 1 sec, Java: 5 sec, Python: 5 sec. C#: 1.5 sec, Haskell: 2 sec, JavaScript: 3
sec, Ruby: 3 sec, Scala: 3 sec.
"""

import random

prime = 10000019 #Prime number needs to be big enough to avoid collision. With prime=10000019, the probability of collision is len(pattern)/10000019, which should be small enough.
x = random.randint(1, prime-1)

def hash(key):
    hashed_value = 0
    for letter in reversed(key):
        hashed_value = hashed_value*x + ord(letter)
        hashed_value = (hashed_value)%prime
    return hashed_value

def find_substring(string, substring):
    searched_hash = hash(substring)
    positions = []
    current_hash = hash(string[len(string)-len(substring):])
    power_of_x = x**(len(substring))
    for index in range(len(string)-len(substring), -1, -1):
        if index < len(string)-len(substring):
            current_hash = (x*current_hash + hash(string[index]) - hash(string[index+len(substring)])*power_of_x )%prime
        if current_hash == searched_hash:
            if string[index:index+len(substring)] == substring:
                positions.append(str(index))
    positions.reverse()
    return positions

substring = input()
string = input()
print(' '.join(find_substring(string, substring)))