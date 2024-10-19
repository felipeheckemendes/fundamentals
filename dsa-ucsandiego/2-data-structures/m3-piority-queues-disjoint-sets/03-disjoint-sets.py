class DisjointSet:
    def __init__(self, size=10):
        self.parent = []
        self.rank = []
        for element in range(size):
            self.parent.append(element)
            self.rank.append(0)
        
    def find_root(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]
        # while self.parent[i] != i:
        #     i = self.parent[i]
        # return i
    
    def merge(self, i, j):
        root_of_i = self.find_root(i)
        root_of_j = self.find_root(j)
        if root_of_i == root_of_j:
            return
        if self.rank[root_of_i] > self.rank[root_of_j]:
            self.parent[root_of_j] = root_of_i
            self.rank[root_of_j] = self.rank[root_of_i]
        elif self.rank[root_of_i] <= self.rank[root_of_j]:
            self.parent[root_of_i] = root_of_j
            if self.rank[root_of_i] == self.rank[root_of_j]:
                self.rank[root_of_j] += 1
    
    def __str__(self):
        return str(self.parent)
    
myset = DisjointSet()
print(myset)
print(myset.rank)

print("\nMerge 0 and 1:")
myset.merge(0, 1)
print(myset)
print(myset.rank)

print("\nMerge 0 and 2:")
myset.merge(0, 2)
print(myset)
print(myset.rank)

print("\nMerge 3 and 4:")
myset.merge(3, 4)
print(myset)
print(myset.rank)

print("\nMerge 0 and 3:")
myset.merge(0, 3)
print(myset)
print(myset.rank)

print("\nFind roots:")
print("Root of 0:", myset.find_root(0))
print("Root of 1:", myset.find_root(1))
print("Root of 2:", myset.find_root(2))
print("Root of 3:", myset.find_root(3))
print("Root of 4:", myset.find_root(4))
    
print("\nCheck wether finding roots has reduced tree height:")
print(myset)
print(myset.rank)    
