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
        self.x = random.randint(1, self.prime-1)
        self.a = random.randint(1, self.prime-1)
        self.b = random.randint(1, self.prime-1)

    def hash(self, key):
        hashed_value = 0
        for letter in reversed(key):
            hashed_value = hashed_value*self.x + ord(letter)
        hashed_value = ((hashed_value*self.a+self.b)%self.prime)%self.size
        return hashed_value
    
    def rehash(self):
        load_factor = self.number_of_keys / self.size
        if load_factor > 0.9:
            print("REHASHING")
            new_table = HashTable(self.size * 2)
            for chain in self.chains:
                for pair in chain:
                    new_table.set_object(pair.key, pair.value)
            self.chains = new_table.chains
            self.size = new_table.size
            self.number_of_keys = new_table.number_of_keys
            self.prime = new_table.prime
            self.x = new_table.x

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
                return element.value
        return None
    
    def set_object(self, key, value):
        self.rehash()
        chain = self.chains[self.hash(key)]
        for element in chain:
            if element.key == key:
                element.value = value
        chain.append(Pair(key, value))
        self.number_of_keys += 1

    def __str__(self):
        string = ''
        for chain in self.chains:
            string += " <-> ".join(map(str, chain)) + " <-> None" + "\n"
        return string


hash_table = HashTable(2)
hash_table.set_object("Gandalf", 111111)
print(hash_table)
hash_table.set_object("Frodo", 222222)
print(hash_table)
hash_table.set_object("Legolas", 333333)
print(hash_table)
hash_table.set_object("Gimli", 444444)
print(hash_table)
hash_table.set_object("Aragorn", 555555)
print(hash_table)