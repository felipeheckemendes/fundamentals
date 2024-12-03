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
            parent.left = node_y
            node_y.parent = parent
        elif parent.right == node:
            parent.right= node_y
            node_y.parent = parent
        elif parent == node:
            node_y.parent = node_y
            self.root = node_y

        node_x.parent = node_y
        node_y.right = node_x

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
            parent.left = node_y
            node_y.parent = parent
        elif parent.right == node:
            parent.right= node_y
            node_y.parent = parent
        elif parent == node:
            node_y.parent = node_y
            self.root = node_y

        node_x.parent = node_y
        node_y.left = node_x

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
        if node.key == 5:
            print("Rebalancing right on node 5")
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
        # print("Rebalance function...")
        # print(self.root.right)
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
#Tree 1
tree1 = BinarySearchTree(Node(1))
inserted = tree1.insert(2)
inserted = tree1.insert(3)
inserted = tree1.insert(4)
inserted = tree1.insert(5)
tree2 = BinarySearchTree(Node(10))
inserted = tree2.insert(20)
inserted = tree2.insert(30)
inserted = tree2.insert(40)
inserted = tree2.insert(50)

print(tree1)
print(tree2)
tree3 = merge_avl(tree1, tree2)
print(tree3)
tree4, tree5 = split_iterative(tree3, 10)
print(tree4)
print(tree5)

# print(tree1)
# tree1.delete(tree1.root)
# print(tree1)