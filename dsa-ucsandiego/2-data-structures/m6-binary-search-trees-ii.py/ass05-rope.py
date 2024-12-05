"""PROBLEM
5 Rope
Problem Introduction
In this problem you will implement Rope — data structure that can store a string and efficiently cut a part (a
substring) of this string and insert it in a different position. This data structure can be enhanced to become
persistent — that is, to allow access to the previous versions of the string. These properties make it a suitable
choice for storing the text in text editors.
This is a very advanced problem, harder than all the previous advanced problems in this course. Don’t be
upset if it doesn’t crack. Congratulations to all the learners who are able to successfully pass this problem!

Problem Description
Task. You are given a string 𝑆 and you have to process 𝑛 queries. Each query is described by three integers
𝑖, 𝑗, 𝑘 and means to cut substring 𝑆[𝑖..𝑗] (𝑖 and 𝑗 are 0-based) from the string and then insert it after the
𝑘-th symbol of the remaining string (if the symbols are numbered from 1). If 𝑘 = 0, 𝑆[𝑖..𝑗] is inserted
in the beginning. See the examples for further clarification.

Input Format. The first line contains the initial string 𝑆.
The second line contains the number of queries 𝑞.
Next 𝑞 lines contain triples of integers 𝑖, 𝑗, 𝑘.

Constraints. 𝑆 contains only lowercase english letters. 1 ≤ |𝑆| ≤ 300 000; 1 ≤ 𝑞 ≤ 100 000; 0 ≤ 𝑖 ≤ 𝑗 ≤
𝑛 − 1; 0 ≤ 𝑘 ≤ 𝑛 − (𝑗 − 𝑖 + 1).

Output Format. Output the string after all 𝑞 queries.
"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.value = value
        self.height = 1
        self.size = 1

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

    def recompute_size(self, node):
        left_size = 0 if node.left == None else node.left.size
        right_size = 0 if node.right == None else node.right.size
        node.size = left_size + right_size + 1
        if node.parent == node:
            return
        else:
            return self.recompute_size(node.parent)

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
        self.recompute_size(node_x)

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
        self.recompute_size(node_x)

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

    def _insert(self, key, value):
        target = self.search_insert_position(key, self.root)
        new_node = Node(key, value)
        if target == None:
            self.root = new_node
            new_node.parent = new_node
            return new_node
        if new_node.key < target.key:
            target.set_left(new_node)
            self.recompute_size(target)
        elif new_node.key >= target.key and target.right == None:
            target.set_right(new_node)
            self.recompute_size(target)
        else:
            target.set_left(new_node)
            self.recompute_size(target)
        self.rebalance(new_node)
        return new_node

    def insert(self, key, value):
        new_node = self._insert(key, value)
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
                self.recompute_size(parent)
            elif parent.right == element_to_delete:
                parent.set_right(None)
                self.recompute_size(parent)
            elif parent == element_to_delete:
                self.root = None
        if right == None or left == None: # If there is only one child
            if left != None:
                if element_to_delete == parent.left:
                    parent.set_left(left)
                    self.recompute_size(parent)
                if element_to_delete == parent.right:
                    parent.set_right(left)
                    self.recompute_size(parent)
                if element_to_delete == parent:
                    self.root = left
                    left.parent = left
                    self.recompute_size(self.root)
                    parent = self.root # TODO or maybe should be parent = next_element
            if right != None:
                if element_to_delete == parent.left:
                    parent.set_left(right)
                    self.recompute_size(parent)
                if element_to_delete == parent.right:
                    parent.set_right(right)
                    self.recompute_size(parent)
                if element_to_delete == parent:
                    self.root = right
                    right.parent = right
                    parent = self.root # TODO or mayve should be parent = next_element
                    self.recompute_size(parent)
        else: # If there are 2 children (in this case, next element does NOT have a left child, but might have a right)
            next_element = element_to_delete.next()
            next_right = next_element.right
            next_left = next_element.left
            next_parent = next_element.parent
            if right != next_element: # If next is not element_to_delete's direct child.
                next_parent.set_left(next_right) # Promote next element's right element
                self.recompute_size(next_parent)
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
                self.recompute_size(next_element)
                self.recompute_size(parent)
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
                self.recompute_size(next_element)
        self.rebalance(parent)
        if next_element != None:
            self.rebalance(next_parent)

    def order_statistics(self, k, node=None):
        if node == None:
            node = self.root
        left_size = 0 if node.left == None else node.left.size
        right_size = 0 if node.right == None else node.right.size
        if k == left_size + 1:
            return node
        elif k < left_size + 1:
            return self.order_statistics(k, node.left)
        elif k > left_size + 1:
            return self.order_statistics(k - left_size - 1, node.right)

    def update_keys(self, starting_key, step, node='tree-root'):
        nodes = []
        if node == 'tree-root':
            node = self.root       
        if node == None:
            return
        new_key = starting_key

        if node.left == None and node.right == None:
            node.key = new_key + step
            return new_key + step

        if node.left != None:
            new_key = self.update_keys(new_key, step, node.left)
        node.key = new_key + step
        if node.right != None:
            new_key += step
            new_key = self.update_keys(new_key, step, node.right)
        return new_key + step

    def in_order_traversal(self, node='tree-root'):
        nodes = []
        if node == 'tree-root':
            node = self.root       
        if node == None:
            return

        if node.left == None and node.right == None:
            return [node.value]

        if node.left != None:
            nodes += self.in_order_traversal(node.left)
        nodes += [node.value]
        if node.right != None:
            nodes += self.in_order_traversal(node.right)
        return nodes

    def __str__(self):
        # Start the string representation from the root node.
        return self._str_helper(self.root, "", True)

    def _str_helper(self, node, prefix, is_left):
        # Base case: if the node is None, return an empty string
        if node is None:
            return ""
        
        # Prepare the current node's string with prefix and node key
        result = prefix + ("├── " if is_left else "└── ") + str(node.value) + '(' + str(node.key) + ', ' + str(node.size) + ")\n"
        
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

def merge_with_root(tree1, tree2, new_root_key, new_root_value):
    tree1_height = 0 if tree1 == None or tree1.root == None else tree1.root.height
    tree2_height = 0 if tree2 == None or tree2.root == None else tree2.root.height
    new_tree = BinarySearchTree(Node(new_root_key, new_root_value))
    new_tree.root.set_left(tree1.root)
    new_tree.root.set_right(tree2.root)
    new_tree.root.height = max(tree1_height, tree2_height) + 1
    return new_tree

def merge(tree1, tree2):
    new_root_node = tree1.search(float('inf'), tree1.root)
    tree1.delete(new_root_node)
    new_tree = merge_with_root(tree1, tree2, new_root_node.key)
    return new_tree

def merge_with_root_avl(tree1, tree2, new_root_key, new_root_value):
    tree1_height = 0 if tree1 == None or tree1.root == None else tree1.root.height
    tree2_height = 0 if tree2 == None or tree2.root == None else tree2.root.height
    if abs(tree1_height - tree2_height) <= 1:
        new_tree = merge_with_root(tree1, tree2, new_root_key, new_root_value)
        new_tree.recompute_size(new_tree.root)
        return new_tree
    elif tree1_height > tree2_height:
        r_prime = merge_with_root_avl(BinarySearchTree(tree1.root.right), tree2, new_root_key, new_root_value)
        tree1.root.set_right(r_prime.root)
        tree1.recompute_size(tree1.root)
        tree1.rebalance(tree1.root)
        return tree1
    elif tree1_height < tree2_height:
        r_prime = merge_with_root_avl(tree1, BinarySearchTree(tree2.root.left), new_root_key, new_root_value)
        tree2.root.set_left(r_prime.root)
        tree2.recompute_size(tree2.root)
        tree2.rebalance(tree2.root)
        return tree2
    
def merge_avl(tree1, tree2):
    if tree1 == None or tree1.root == None:
        return tree2
    if tree2 == None or tree2.root == None:
        return tree1
    new_root_node = tree1.search(float('inf'), tree1.root)
    boolean = False
    tree1.delete(new_root_node)
    new_tree = merge_with_root_avl(tree1, tree2, new_root_node.key, new_root_node.value)
    return new_tree

def split(tree, key):
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

def split_iterative(tree, key):
    current = tree.root
    smaller_tree = BinarySearchTree(None)
    bigger_tree = BinarySearchTree(None)
    while current.left != None or current.right != None or key == current.key:
        if key > current.key:
            new_tree = BinarySearchTree(current.right)
            current.right = None
            tree.recompute_size(current)
            smaller_tree = merge_avl(smaller_tree, BinarySearchTree(current))
            current = new_tree.root
            separating_element = BinarySearchTree(None)
            # if current.right == None:
            #     current.root = Node(key)
        elif key < current.key:
            new_tree = BinarySearchTree(current.left)
            current.left = None
            tree.recompute_size(current)
            bigger_tree = merge_avl(BinarySearchTree(current), bigger_tree)
            current = new_tree.root
            separating_element = BinarySearchTree(None)
            # if current.left == None:
            #     current.root = Node(key)
        elif key == current.key:
            smaller_tree = merge_avl(smaller_tree, BinarySearchTree(current.left))
            bigger_tree = merge_avl(BinarySearchTree(current.right), bigger_tree)
            current.set_left(None)
            current.set_right(None)
            separating_element = BinarySearchTree(current)
            current = Node(None, None)
    return (separating_element, smaller_tree, bigger_tree)

def main():
    string = input()
    n = int(input())
    key = 12
    tree = BinarySearchTree(None)
    for letter in string:
        tree.insert(key, letter)
        key += 12

    commands = []
    for _ in range(n):
        commands.append(input().split()[:3])

    for command in commands:
        i, j, k = map(int, command)
        node_i = tree.order_statistics(i+1)
        node_j = tree.order_statistics(j+1)

        # Remove the i-j string from the tree
        first_letter, left, right = split_iterative(tree, node_i.key)
        if j > i:
            last_letter, middle_letters, right = split_iterative(right, node_j.key)
        else:
            last_letter = BinarySearchTree(None)
            middle_letters = BinarySearchTree(None)
        word_tree = merge_avl(first_letter, middle_letters)
        word_tree = merge_avl(word_tree, last_letter)
        remaining_tree = merge_avl(left, right)
        
        if k > 0: # If insert position is on the middle, split
            # Compute the new starting_value for the first letter of the tree & the step for all subsequent letters
            node_k = remaining_tree.order_statistics(k)
            node_k_next = node_k.next()
            starting_key = node_k.key
            step = (node_k_next.key - node_k.key)/(j-i+1+1)
            # Update the word_tree's values (in-order traversal) so that they fall between k and its next element
            word_tree.update_keys(starting_key, step)
            # Split remaining tree on position to insert and merge to insert
            splitting, left, right = split_iterative(remaining_tree, node_k.key)
            left = merge_avl(left, splitting)
            new_tree = merge_avl(left, word_tree)
            new_tree = merge_avl(new_tree, right)
        else: # if k == 0: If insert position is before, merge word on left with remaining on right
            node_k = remaining_tree.order_statistics(1)
            starting_key = node_k.key - 12
            step = -12
            word_tree.update_keys(starting_key, step)
            new_tree = merge_avl(word_tree, remaining_tree)
        tree = new_tree
    print(''.join(new_tree.in_order_traversal()))
main()