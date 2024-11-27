from collections import deque
import random

class Element:
    def __init__(self, key):
        self.key = key
    def __str__(self):
        return str(self.key)

class HashTable:
    def __init__(self, cardinality):
        self.chains = [deque() for _ in range(cardinality)]
        self.size = cardinality
        self.number_of_keys = 0
        self.prime = 1000000007
        self.x = 263

    def hash(self, key):
        hashed_value = 0
        for letter in reversed(key):
            hashed_value = hashed_value*self.x + ord(letter)
        hashed_value = ((hashed_value)%self.prime)%self.size
        return hashed_value

    def has_key(self, key):
        chain = self.chains[self.hash(key)]
        for element in chain:
            if element.key == key:
                return True
        return False
    
    def get_value(self, key):
        chain = self.chains[self.hash(key)]
        for element in chain:
            if element.key == key:
                return 'yes'
        return 'no'
    
    def set_object(self, key):
        chain = self.chains[self.hash(key)]
        for element in chain:
            if element.key == key:
                return
        chain.insert(0, Element(key))
        self.number_of_keys += 1

    def remove_object(self, key):
        chain = self.chains[self.hash(key)]
        for element in chain:
            if element.key == key:
                chain.remove(element)
                break

    def __str__(self):
        string = ''
        for chain in self.chains:
            string += " ".join(map(str, chain)) + "\n"
        return string
    
    def check_position(self, position):
        return " ".join(map(str, self.chains[position]))

m = int(input())
hash_table = HashTable(m)
n = int(input())
output = []
for _ in range(n):
    action, value = input().split()[:2]
    if action == 'add':
        hash_table.set_object(value)
    if action == 'check':
        output.append(hash_table.check_position(int(value)))
    if action == 'find':
        output.append(hash_table.get_value(value))
    if action == 'del':
        hash_table.remove_object(value)
for line in output:
    print(line)