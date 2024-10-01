class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def node_height(self):
        if len(self.children) == 0:
            return 1
        return 1 + max(child.node_height() for child in self.children)

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