"""PROBLEM
4.3.7 Anagram Search
Anagram Search Problem
Given a set of strings, check whether it contains a pair of strings that form an anagram.
Input: A set of strings. 
Output: Check whether this set contains a pair of strings that form an anagram, i.e., formed by the same set of symbols.
"""
"""SOLUTION
The solution for this problem involves mapping the array os string using a function that returns the same value for words with same letters.
This function must be some kind of count of letters.
We choose a function that converts the string into another string, where each position is the count of letters of that index on the alphabet.
Solution limitation: only letters on the string (that is, only words)
"""
def  find_anagrams(arr):
    arr = [letter_count(element) for element in arr]
    count = {}
    for element in arr:
        if element in count:
            return True
        else:
            count[element] = True
    return False

def letter_count(string):
    letter_positions = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
    }
    result = [0 for element in range(26)]
    for character in string:
        result[letter_positions[character]] += 1
    return ''.join(list(map(str, result)))

print(find_anagrams(['stamp', 'taste', 'pasta', 'paste', 'taste']))