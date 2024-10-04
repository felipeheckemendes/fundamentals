import math
from io import StringIO

class PriorityQueue:
    def __init__(self, max_size=100, size=0):
        self.max_size = max_size
        self.size = size
        self.arr = [None]*max_size
    
    def left_child_index(self, index):
        if (index + 1)*2-1 < self.size:
            return (index + 1)*2-1
        else:
            return index

    def right_child_index(self, index):
        if (index + 1)*2 < self.size:
            return (index + 1)*2
        else:
            return index

    def parent_index(self, index):
        if index > 0:
            return (index-1)//2
        else:
            return 0

    def swap(self, index1, index2):
        self.arr[index1], self.arr[index2] = self.arr[index2], self.arr[index1]

    def sift_up(self, index):
        parent = self.parent_index(index)
        while self.arr[parent] < self.arr[index]:
            self.swap(parent, index)
            index = parent
            parent = self.parent_index(index)

    def sift_down(self, index):
        left_child = self.left_child_index(index)
        right_child = self.right_child_index(index)
        while self.arr[left_child] > self.arr[index] or self.arr[right_child] > self.arr[index]:
            if self.arr[left_child] >= self.arr[right_child]:
                self.swap(left_child, index)
                index = left_child
                left_child = self.left_child_index(index)
                right_child = self.right_child_index(index)
            else:
                self.swap(right_child, index)
                index = right_child
                left_child = self.left_child_index(index)
                right_child = self.right_child_index(index)

    def max(self):
        return self.arr[0]

    def extract_max(self):
        if self.size <= 0:
            return "Error, no elements to remove"
        self.swap(0, self.size-1)
        self.size -= 1
        self.sift_down(0)
        return self.arr[self.size]
    
    def add_element(self, element):
        if self.size < self.max_size:
            self.arr[self.size] = element
            self.size += 1
            self.sift_up(self.size-1)
        else:
            print("ERROR, not possible to add", element, ":array full")

    def show_tree(self, tree=None, total_width=None, fill=' '):
        if total_width is None:
            total_width = 2 ** ((self.size - 1).bit_length())
        tree = self.arr[:self.size]
        """Pretty-print a tree.
        total_width depends on your input size"""
        output = StringIO()
        last_row = -1
        for i, n in enumerate(tree):
            if i:
                row = int(math.floor(math.log(i+1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2**row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print (output.getvalue())
        print ('-' * total_width)
        return

# Testing
myheap = PriorityQueue()
myheap.add_element(1)
myheap.add_element(2)
myheap.add_element(3)
myheap.add_element(4)
myheap.add_element(5)
myheap.add_element(6)
myheap.add_element(7)
myheap.add_element(8)
myheap.show_tree()
print("Extracted:", myheap.extract_max())
print("Extracted:", myheap.extract_max())
print("Extracted:", myheap.extract_max())
print("Extracted:", myheap.extract_max())
print("Extracted:", myheap.extract_max())
myheap.show_tree()
print("Extracted:", myheap.extract_max())
print("Extracted:", myheap.extract_max())
print("Extracted:", myheap.extract_max())
myheap.show_tree()
print("Extracted:", myheap.extract_max())
