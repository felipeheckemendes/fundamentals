from collections import deque

class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ": " + str(self.value)

CARDINALITY = 10
class HashTable:
    def hash(self, key):
        return key%10

    def __init__(self):
        self.chains = [deque() for _ in range(CARDINALITY)]

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
        chain = self.chains[self.hash(key)]
        for element in chain:
            if element.key == key:
                element.value = value
        chain.append(Pair(key, value))


hash_table = HashTable()
hash_table.set_object(101, "Hello")
hash_table.set_object(102, "Bye")
hash_table.set_object(1, "Hello 2")
hash_table.set_object(10001, "Hello 3")
print(hash_table.get_value(101))
print(hash_table.get_value(102))
print(hash_table.has_key(10001))
print(hash_table.has_key(10002))
print(" <-> ".join(map(str, hash_table.chains[1])) + " <-> None")
print(" <-> ".join(map(str, hash_table.chains[2])) + " <-> None")