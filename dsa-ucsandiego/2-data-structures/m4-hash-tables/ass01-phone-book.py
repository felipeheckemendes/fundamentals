"""PROBLEM
Problem Introduction
In this problem you will implement a simple phone book manager.

Problem Description
Task. 
In this task your goal is to implement a simple phone book manager. It should be able to process the following types of user’s queries:
- add number name. It means that the user adds a person with name name and phone number
number to the phone book. If there exists a user with such number already, then your manager
has to overwrite the corresponding name.
- del number. It means that the manager should erase a person with number number from the phone
book. If there is no such person, then it should just ignore the query.
- find number. It means that the user looks for a person with phone number number. The manager
should reply with the appropriate name, or with string “not found" (without quotes) if there is
no such person in the book.

Input Format. There is a single integer 𝑁 in the first line — the number of queries. It’s followed by 𝑁
lines, each of them contains one query in the format described above.

Constraints. 1 ≤ 𝑁 ≤ 10**5. All phone numbers consist of decimal digits, they don’t have leading zeros, and
each of them has no more than 7 digits. All names are non-empty strings of latin letters, and each of
them has length at most 15. It’s guaranteed that there is no person with name “not found".

Output Format. Print the result of each find query — the name corresponding to the phone number or
“not found" (without quotes) if there is no person in the phone book with such phone number. Output
one result per line in the same order as the find queries are given in the input.
"""

from collections import deque
import random

class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ": " + str(self.value)

class HashTable:
    def __init__(self, cardinality):
        self.chains = [deque() for _ in range(cardinality)]
        self.size = cardinality
        self.number_of_keys = 0
        self.prime = 10000019 #Prime number needs to be bigger than the the largests phone number to be hashed. In our case, since telephone numbers have 7 digitis, it needs to be bigger than 9.999.999
        self.a = random.randint(1, self.prime-1)
        self.b = random.randint(1, self.prime-1)

    def hash(self, key):
        return ((self.a*key+self.b)%self.prime)%self.size
    
    def rehash(self):
        load_factor = self.number_of_keys / self.size
        if load_factor > 0.9:
            new_table = HashTable(self.size * 2)
            for chain in self.chains:
                for pair in chain:
                    new_table.set_object(pair.key, pair.value)
            self.chains = new_table.chains
            self.size = new_table.size
            self.number_of_keys = new_table.number_of_keys
            self.prime = new_table.prime
            self.a = new_table.a
            self.b = new_table.b
    
    def get_value(self, key):
        chain = self.chains[self.hash(key)]
        for element in chain:
            if element.key == key:
                return element.value
        return "not found"
    
    def set_object(self, key, value):
        self.rehash()
        chain = self.chains[self.hash(key)]
        for element in chain:
            if element.key == key:
                element.value = value
        chain.append(Pair(key, value))
        self.number_of_keys += 1

    def remove_object(self, key):
        chain = self.chains[self.hash(key)]
        for element in chain:
            if element.key == key:
                chain.remove(element)
                break

phone_book = HashTable(2)
n = int(input())
found = []
for i in range(n):
    command = input().split()
    if len(command) == 2:
        action, number = command
    elif len(command) == 3:
        action, number, name = command
    if action == 'add':
        phone_book.set_object(int(number), name)
    elif action == 'find':
        found.append(phone_book.get_value(int(number)))
    elif action == 'del':
        phone_book.remove_object(int(number))

for element in found:
    print(element)