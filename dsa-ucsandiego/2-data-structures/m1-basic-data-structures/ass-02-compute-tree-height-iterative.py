class QueueNode:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self):
        if self == None:
            return 'None'
        string = str(self.value) + ' -> '
        return string

class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, value):
        new_node = QueueNode(value)
        if self.head != None:
            self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = self.head

    def top_front(self):
        return self.head.value   
    
    def top_back(self):
        return self.tail.value

    def dequeue(self):
        if self.tail == None:
            print("Error, empty list")
            return
        if self.head == self.tail:
            dequeued = self.tail
            self.head = self.tail = None
        else:
            dequeued = self.tail
            self.tail.previous.next = None
            self.tail = self.tail.previous
        return dequeued
    
    def is_empty(self):
        if self.head == self.tail == None:
            return True
        else:
            return False
    
    def __str__(self):
        string1 = 'In'
        current_node = self.head
        while current_node != None:
            string1 += ' -> ' + str(current_node.value)
            current_node = current_node.next
        string1 += ' -> Out'
        return string1

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def node_height(self):
        queue = Queue()
        queue.enqueue([self, 1])
        max_height = 1
        while not queue.is_empty():
            current_node, height = queue.dequeue().value
            max_height = max(max_height, height)
            for child in current_node.children:
                queue.enqueue([child, height+1])
        return max_height

class Tree:
    def __init__(self, root_node):
        self.root = root_node

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        # Print the current node value with indentation based on level
        print(' ' * (level) + str(node.value))
        # Recursively print each child
        for child in node.children:
            self.print_tree(child, level + 1)

    def height(self):
        height = self.root.node_height()
        return height

number_of_nodes = int(input())
input_list = list(map(int, input().split()))
nodes = []
for value in range(number_of_nodes):
    nodes.append(Node(value))
for order, parent in enumerate(input_list):
    if parent == -1:
        mytree = Tree(nodes[order])
    if parent != -1:
        nodes[parent].add_child(nodes[order])

print(mytree.height())