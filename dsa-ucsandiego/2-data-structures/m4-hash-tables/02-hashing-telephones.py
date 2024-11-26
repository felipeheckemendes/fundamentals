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
            print("REHASHING")
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
hash_table.set_object(111111, "Name A")
print(hash_table)
hash_table.set_object(222222, "Name B")
print(hash_table)
hash_table.set_object(333333, "Name C")
print(hash_table)
hash_table.set_object(444444, "Name D")
print(hash_table)
hash_table.set_object(555555, "Name E")
print(hash_table)