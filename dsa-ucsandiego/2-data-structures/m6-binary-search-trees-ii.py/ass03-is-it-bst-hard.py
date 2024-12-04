"""PROBLEM
3 Is it a binary search tree? Hard version.

Problem Introduction
In this problem you are going to solve the same problem as the previous one, but for a more general case,
when binary search tree may contain equal keys.

Problem Description
Task. You are given a binary tree with integers as its keys. You need to test whether it is a correct binary
search tree. Note that there can be duplicate integers in the tree, and this is allowed. The definition of
the binary search tree in such case is the following: for any node of the tree, if its key is 𝑥, then for any
node in its left subtree its key must be strictly less than 𝑥, and for any node in its right subtree its key
must be greater than or equal to 𝑥. In other words, smaller elements are to the left, bigger elements
are to the right, and duplicates are always to the right. You need to check whether the given binary
tree structure satisfies this condition. You are guaranteed that the input contains a valid binary tree.
That is, it is a tree, and each node has at most two children.

Input Format. The first line contains the number of vertices 𝑛. The vertices of the tree are numbered
from 0 to 𝑛 − 1. Vertex 0 is the root.
The next 𝑛 lines contain information about vertices 0, 1, ..., 𝑛−1 in order. Each of these lines contains
three integers 𝑘𝑒𝑦𝑖, 𝑙𝑒𝑓𝑡𝑖 and 𝑟𝑖𝑔ℎ𝑡𝑖 — 𝑘𝑒𝑦𝑖 is the key of the 𝑖-th vertex, 𝑙𝑒𝑓𝑡𝑖 is the index of the left
child of the 𝑖-th vertex, and 𝑟𝑖𝑔ℎ𝑡𝑖 is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have
left or right child (or both), the corresponding 𝑙𝑒𝑓𝑡𝑖 or 𝑟𝑖𝑔ℎ𝑡𝑖 (or both) will be equal to −1.

Constraints. 0 ≤ 𝑛 ≤ 10**5; −2**31 ≤ 𝑘𝑒𝑦𝑖 ≤ 2**31 − 1; −1 ≤ 𝑙𝑒𝑓𝑡𝑖, 𝑟𝑖𝑔ℎ𝑡𝑖 ≤ 𝑛 − 1. It is guaranteed that the
input represents a valid binary tree. In particular, if 𝑙𝑒𝑓𝑡𝑖 ̸= −1 and 𝑟𝑖𝑔ℎ𝑡𝑖 ̸= −1, then 𝑙𝑒𝑓𝑡𝑖 ̸= 𝑟𝑖𝑔ℎ𝑡𝑖.
Also, a vertex cannot be a child of two different vertices. Also, each vertex is a descendant of the root
vertex. Note that the minimum and the maximum possible values of the 32-bit integer type are allowed
to be keys in the tree — beware of integer overflow!

Output Format. If the given binary tree is a correct binary search tree (see the definition in the problem
description), output one word “CORRECT” (without quotes). Otherwise, output one word “INCORRECT”
(without quotes).
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

    def next(self):
        if self.right == None:
            return self.right_ancestor()
        else:
            return self.right.left_descendant()
    
    def left_descendant(self):
        if self.left == None:
            return self
        else:
            return self.left.left_descendant()
        
    def right_ancestor(self):
        if self.parent.key >= self.key:
            return self.parent
        elif self.parent.key < self.key:
            return self.parent.right_ancestor()

    def set_left(self, node):
        self.left = node
        if node != None:
            node.parent = self
    
    def set_right(self, node):
        self.right = node
        if node != None:
            node.parent = self

    def __str__(self):
        # Start the string representation from the root node.
        return str(self.key)

class BinarySearchTree:
    def __init__(self, root):
        self.root = root
        if self.root:
            self.root.parent = self.root

    def search(self, value, node):
        if node == None:
            return None
        if node.key == value:
            return node
        elif node.key > value:
            if node.left != None:
                return self.search(value, node.left)
            return node
        elif node.key < value:
            if node.right != None:
                return self.search(value, node.right)
            return node

    def search_insert_position(self, value, node):
        if node == None:
            return None
        if node.key == value:
            if node.right != None and node.right.key == value:
                return self.search_insert_position(value, node.right)
            elif node.left != None and node.left.key == value:
                return self.search_insert_position(value, node.left)
            elif node.right != None and node.left != None:
                return self.search_insert_position(value, node.right)
            return node
        elif value < node.key:
            if node.left != None:
                return self.search_insert_position(value, node.left)
            return node
        elif value > node.key:
            if node.right != None:
                return self.search_insert_position(value, node.right)
            return node

    def range_search(self, x, y):
        if x > y:
            return []
        range_elements = []
        first_element = self.search(x, self.root)
        range_elements.append(first_element)
        next_element = first_element.next()
        while next_element != None and next_element.key <= y:
            range_elements.append(next_element)
            next_element = next_element.next()
        for element in range_elements:
            if not x<= element.key <= y:
                range_elements.remove(element)
        return range_elements

    def rotate_right(self, node):
        if node.left == None:
            print("Not possible to rotate right if node does not have left element")
            return
        node_x = node
        parent = node.parent
        node_y = node.left
        node_b = node_y.right

        if parent.left == node:
            parent.set_left(node_y)
        elif parent.right == node:
            parent.set_right(node_y)
        elif parent == node:
            self.root = node_y
            node_y.parent = node_y
        node_y.set_right(node_x)
        if node_b != None:
            node_b.parent = node_x
        node_x.left = node_b

        self.adjust_height(node)
        self.adjust_height(node.parent)

    def rotate_left(self, node):
        if node.right == None:
            print("Not possible to rotate left if node does not have right element")
            return
        node_x = node
        parent = node.parent
        node_y = node.right
        node_b = node_y.left

        if parent.left == node:
            parent.set_left(node_y)
        elif parent.right == node:
            parent.set_right(node_y)
        elif parent == node:
            self.root = node_y
            node_y.parent = node_y
        node_y.set_left(node_x)
        if node_b != None:
            node_b.parent = node_x
        node_x.right = node_b

        self.adjust_height(node)
        self.adjust_height(node.parent)

    def adjust_height(self, node):
        left_height = 0 if node.left == None else node.left.height
        right_height = 0 if node.right == None else node.right.height
        node.height = 1 + max(left_height, right_height)

    def rebalance_right(self, node):
        node_a = node.left
        node_a_left_height = 0 if node_a.left == None else node_a.left.height
        node_a_right_height = 0 if node_a.right == None else node_a.right.height
        if node_a_right_height > node_a_left_height:
            self.rotate_left(node_a)
        self.rotate_right(node)

    def rebalance_left(self, node):
        node_a = node.right
        node_a_left_height = 0 if node_a.left == None else node_a.left.height
        node_a_right_height = 0 if node_a.right == None else node_a.right.height
        if node_a_left_height > node_a_right_height:
            self.rotate_right(node_a)
        self.rotate_left(node)

    def rebalance(self, node):
        parent = node.parent
        left_height = 0 if node.left == None else node.left.height
        right_height = 0 if node.right == None else node.right.height
        if left_height > right_height + 1:
            self.rebalance_right(node)
        elif right_height > left_height + 1:
            self.rebalance_left(node)
        self.adjust_height(node)
        if parent != node: # If not the root yet, propage rebalance up
            self.rebalance(parent)

    def _insert(self, key):
        target = self.search_insert_position(key, self.root)
        new_node = Node(key)
        if target == None:
            self.root = new_node
            new_node.parent = new_node
            return
        if new_node.key < target.key:
            target.set_left(new_node)
        elif new_node.key >= target.key and target.right == None:
            target.set_right(new_node)
        else:
            target.set_left(new_node)
        self.rebalance(new_node)
        return new_node

    def insert(self, key):
        new_node = self._insert(key)
        self.rebalance(new_node)
        return new_node

    def remove_key(self, key):
        element_to_delete = self.search(key, self.root)
        if element_to_delete.key != key:
            return
        else:
            self.delete(element_to_delete)

    def delete(self, element_to_delete):
        if element_to_delete == None:
            return
        parent = element_to_delete.parent
        right = element_to_delete.right
        left = element_to_delete.left
        next_element = None

        if right == None and left == None: # If it is a leaf 
            if parent.left == element_to_delete:
                parent.set_left(None)
            elif parent.right == element_to_delete:
                parent.set_right(None)
            elif parent == element_to_delete:
                self.root = None
        if right == None or left == None: # If there is only one child
            if left != None:
                if element_to_delete == parent.left:
                    parent.set_left(left)
                if element_to_delete == parent.right:
                    parent.set_right(left)
                if element_to_delete == parent:
                    self.root = left
                    left.parent = left
                    parent = self.root # TODO or mayve should be parent = next_element
            if right != None:
                if element_to_delete == parent.left:
                    parent.set_left(right)
                if element_to_delete == parent.right:
                    parent.set_right(right)
                if element_to_delete == parent:
                    self.root = right
                    right.parent = right
                    parent = self.root # TODO or mayve should be parent = next_element
        else: # If there are 2 children (in this case, next element does NOT have a left child, but might have a right)
            next_element = element_to_delete.next()
            next_right = next_element.right
            next_left = next_element.left
            next_parent = next_element.parent
            if right != next_element: # If next is not element_to_delete's direct child.
                next_parent.set_left(next_right) # Promote next element's right element
                # Replace element to delete with next element (2 steps: Set it as child of element_to_delete's parent, and set it is right and left equal to element_to_delete's right and left)
                if element_to_delete == parent.left: # 1st step
                    parent.set_left(next_element)
                if element_to_delete == parent.right:
                    parent.set_right(next_element)
                if element_to_delete == parent:
                    self.root = next_element
                    next_element.parent = next_element
                    parent = next_element
                next_element.set_right(right) # 2nd step
                next_element.set_left(left)
            else: # If it is the direct child
                if element_to_delete == parent.left:
                    parent.set_left(next_element)
                if element_to_delete == parent.right:
                    parent.set_right(next_element)
                if element_to_delete == parent:
                    self.root = next_element
                    next_element.parent = next_element
                    parent = next_element
                next_element.set_left(left)
        self.rebalance(parent)
        if next_element != None:
            self.rebalance(next_parent)

    def in_order_traversal(self, node='tree-root'):
        nodes = []
        if node == 'tree-root':
            node = self.root       
        if node == None:
            return

        if node.left == None and node.right == None:
            return [node.key]

        if node.left != None:
            nodes += self.in_order_traversal(node.left)
        nodes += [node.key]
        if node.right != None:
            nodes += self.in_order_traversal(node.right)
        return nodes

    def pre_order_traversal(self, node='tree-root'):
        nodes = []
        if node == 'tree-root':
            node = self.root       
        if node == None:
            return

        if node.left == None and node.right == None:
            return [node.key]

        nodes += [node.key]
        if node.left != None:
            nodes += self.pre_order_traversal(node.left)
        if node.right != None:
            nodes += self.pre_order_traversal(node.right)
        return nodes

    def post_order_traversal(self, node='tree-root'):
        nodes = []
        if node == 'tree-root':
            node = self.root       
        if node == None:
            return

        if node.left == None and node.right == None:
            return [node.key]

        if node.left != None:
            nodes += self.post_order_traversal(node.left)
        if node.right != None:
            nodes += self.post_order_traversal(node.right)
        nodes += [node.key]
        return nodes

    def is_binary_search_tree(self, node='tree-root'):
        nodes = []
        if node == 'tree-root':
            node = self.root       
        if node == None:
            return (None, None, True)

        if node.left == None and node.right == None:
            return (node.key, node.key, True)

        minimum_left = float('inf')
        minimum_right = float('inf')
        maximum_left = float('-inf')
        maximum_right = float('-inf')

        if node.left != None:
            left_result = self.is_binary_search_tree(node.left)
            minimum_left, maximum_left, boolean_left = left_result
            if maximum_left < node.key and boolean_left:
                boolean = True
            else:
                boolean = False
        else:
            boolean = True

        if node.right != None:
            right_result = self.is_binary_search_tree(node.right)
            minimum_right, maximum_right, boolean_right = right_result
            if minimum_right >= node.key and boolean_right and boolean:
                boolean = True
            else:
                boolean = False
        
        minimum = min(minimum_left, minimum_right, node.key)
        maximum = max(maximum_left, maximum_right, node.key)
        return (minimum, maximum, boolean)


    def __str__(self):
        # Start the string representation from the root node.
        return self._str_helper(self.root, "", True)

    def _str_helper(self, node, prefix, is_left):
        # Base case: if the node is None, return an empty string
        if node is None:
            return ""
        
        # Prepare the current node's string with prefix and node key
        result = prefix + ("├── " if is_left else "└── ") + str(node.key) + '(' + str(node.height) + ")\n"
        
        # Recursively call for the left and right children, adjusting the prefix
        # If there are both left and right children, we'll first print the left side,
        # and then print the right side with adjusted prefix to ensure correct structure.
        if node.left or node.right:
            if node.left:
                result += self._str_helper(node.left, prefix + ("│   " if is_left else "    "), True)
            else:
                # When there's no left child, print a placeholder to maintain the structure
                result += prefix + ("│   " if is_left else "    ") + "├── " + "-" + "\n"
            
            if node.right:
                result += self._str_helper(node.right, prefix + ("│   " if is_left else "    "), False)
            else:
                # When there's no right child, print a placeholder to maintain the structure
                result += prefix + ("│   " if is_left else "    ") + "└── " + "-" + "\n"
        
        return result

def merge_with_root(tree1, tree2, new_root_key):
    tree1_height = 0 if tree1 == None or tree1.root == None else tree1.root.height
    tree2_height = 0 if tree2 == None or tree2.root == None else tree2.root.height
    new_tree = BinarySearchTree(Node(new_root_key))
    new_tree.root.set_left(tree1.root)
    new_tree.root.set_right(tree2.root)
    new_tree.root.height = max(tree1_height, tree2_height) + 1
    return new_tree

def merge(tree1, tree2):
    new_root_node = tree1.search(float('inf'), tree1.root)
    tree1.delete(new_root_node)
    new_tree = merge_with_root(tree1, tree2, new_root_node.key)
    return new_tree

def merge_with_root_avl(tree1, tree2, new_root_key):
    tree1_height = 0 if tree1 == None or tree1.root == None else tree1.root.height
    tree2_height = 0 if tree2 == None or tree2.root == None else tree2.root.height
    if abs(tree1_height - tree2_height) <= 1:
        new_tree = merge_with_root(tree1, tree2, new_root_key)
        return new_tree
    elif tree1_height > tree2_height:
        r_prime = merge_with_root_avl(BinarySearchTree(tree1.root.right), tree2, new_root_key)
        tree1.root.set_right(r_prime.root)
        tree1.rebalance(tree1.root)
        return tree1
    elif tree1_height < tree2_height:
        r_prime = merge_with_root_avl(BinarySearchTree(tree2.root.left), tree1, new_root_key)
        tree2.root.set_left(r_prime.root)
        tree2.rebalance(tree2.root)
        return tree2
    
def merge_avl(tree1, tree2):
    if tree1 == None or tree1.root == None:
        return tree2
    if tree2 == None or tree2.root == None:
        return tree1
    new_root_node = tree1.search(float('inf'), tree1.root)
    tree1.delete(new_root_node)
    new_tree = merge_with_root_avl(tree1, tree2, new_root_node.key)
    return new_tree

def split(tree, value):
    if tree == None:
        return (None, None)
    if value < tree.root.key:
        tree1, tree2 = split(BinarySearchTree(tree.root.left), value)
        tree3 = merge_with_root_avl(tree2, BinarySearchTree(tree.root.right), tree.root.key)
        return (tree1, tree3)
    elif value > tree.root.key:
        tree1, tree2 = split(BinarySearchTree(tree.root.right), value)
        tree3 = merge_with_root_avl(BinarySearchTree(tree.root.left), tree2, tree.root.key)
        return (tree1, tree3)
    elif value == tree.root.key:
        tree_smaller = BinarySearchTree(tree.root.left)
        tree.root.set_left(None)
        return (tree_smaller, tree)

def split_iterative(tree, value):
    current = tree.root
    smaller_tree = BinarySearchTree(None)
    bigger_tree = BinarySearchTree(None)
    while current.left != None or current.right != None:
        if value > current.key:
            new_tree = BinarySearchTree(current.right)
            current.right = None
            smaller_tree = merge_avl(smaller_tree, BinarySearchTree(current))
            current = new_tree.root
            if current.right == None:
                current.root = Node(value)
        elif value < current.key:
            new_tree = BinarySearchTree(current.left)
            current.left = None
            bigger_tree = merge_avl(BinarySearchTree(current), bigger_tree)
            current = new_tree.root
            if current.left == None:
                current.root = Node(value)
        elif value == current.key:
            smaller_tree = merge_avl(smaller_tree, BinarySearchTree(current.left))
            bigger_tree = merge_avl(BinarySearchTree(current.right), bigger_tree)
            current.set_left(None)
            current.set_right(None)
    return (smaller_tree, bigger_tree)

def main():
    n = int(input())
    nodes = []
    lefts = []
    rights = []
    for _ in range(n):
        key, left, right = map(int, input().split()[:3])
        node = Node(key)
        nodes.append(node)
        lefts.append(left)
        rights.append(right)

    if len(nodes) == 0:
        print("CORRECT")
        return
        
    tree = BinarySearchTree(nodes[0])
    nodes[0].parent = nodes[0]
    for index in range(len(nodes)):
        if lefts[index] > -1:
            nodes[index].set_left(nodes[lefts[index]])
        if rights[index] > -1:
            nodes[index].set_right(nodes[rights[index]])

    if tree.is_binary_search_tree()[2] == True:
        print("CORRECT")
    else:
        print("INCORRECT")

main()