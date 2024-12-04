class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

    def next(self):
        if self.right == None:
            right_ancestor = self.right_ancestor()
            if right_ancestor.key < self.key:
                return None
            else:
                return right_ancestor
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
        if type(root) == int:
            root = Node(root)
        self.root = root
        if self.root:
            self.root.parent = self.root

    def _search(self, value, node='tree-root'):
        if node == None:
            return None
        if node == 'tree-root':
            node = self.root
        if node.key == value:
            return node
        elif node.key > value:
            if node.left != None:
                return self._search(value, node.left)
            return node
        elif node.key < value:
            if node.right != None:
                return self._search(value, node.right)
            return node

    def search(self, value, node='tree-root'):
        element = self._search(value, node)
        self.splay(element)
        return element

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

    def insert_splay(self, key):
        new_node = self._insert(key)
        self.splay(new_node)
        return new_node
   
    def delete_splay(self, value_to_delete):
        element_to_delete = self._search(value_to_delete)
        if element_to_delete.key != value_to_delete:
            return
        next_element = element_to_delete.next()
        if next_element == None:
            self.splay(element_to_delete)
            left = element_to_delete.left
            self.root = left
            left.parent = left
        elif next_element != None:
            self.splay(next_element)
            self.splay(element_to_delete)
            left = element_to_delete.left
            right = element_to_delete.right
            right.set_left(left)
            self.root = right
            right.parent = right

    def splay(self, node):
        parent = node.parent
        grand_parent = parent.parent
        # Determine if zig, zig-zag or zig case
        # Apply the rearrangement as appropriate
        if (parent.left == node and grand_parent.left == parent): # Zig zig left
            green = node.right
            blue = parent.right
            if grand_parent.parent.left == grand_parent:
                grand_parent.parent.set_left(node)
            elif grand_parent.parent.right == grand_parent:
                grand_parent.parent.set_right(node)
            elif grand_parent.parent == grand_parent:
                self.root = node
                node.parent = node
            node.set_right(parent)
            parent.set_left(green)
            parent.set_right(grand_parent)
            grand_parent.set_left(blue)
        elif (parent.right == node and grand_parent.right == parent): # zig zig right
            green = parent.left
            blue = node.left
            if grand_parent.parent.left == grand_parent:
                grand_parent.parent.set_left(node)
            elif grand_parent.parent.right == grand_parent:
                grand_parent.parent.set_right(node)
            elif grand_parent.parent == grand_parent:
                self.root = node
                node.parent = node
            node.set_left(parent)
            parent.set_right(blue)
            parent.set_left(grand_parent)
            grand_parent.set_right(green)
        elif (parent.right == node and grand_parent.left == parent): # Zig zag left
            green = node.left
            blue = node.right
            if grand_parent.parent.left == grand_parent:
                grand_parent.parent.set_left(node)
            elif grand_parent.parent.right == grand_parent:
                grand_parent.parent.set_right(node)
            elif grand_parent.parent == grand_parent:
                self.root = node
                node.parent = node
            node.set_left(parent)
            node.set_right(grand_parent)
            parent.set_right(green)
            grand_parent.set_left(blue)
        elif (parent.left == node and grand_parent.right == parent): # Zig zag right
            green = node.right
            blue = node.left
            if grand_parent.parent.left == grand_parent:
                grand_parent.parent.set_left(node)
            elif grand_parent.parent.right == grand_parent:
                grand_parent.parent.set_right(node)
            elif grand_parent.parent == grand_parent:
                self.root = node
                node.parent = node
            node.set_left(grand_parent)
            node.set_right(parent)
            parent.set_left(green)
            grand_parent.set_right(blue)
        elif parent.left == node and parent == grand_parent: # Zig left
            green = node.right
            node.set_right(parent)
            parent.set_left(green)
            self.root = node
            node.parent = node
        elif parent.right == node and parent == grand_parent: # Zig right 
            green = node.left
            node.set_left(parent)
            parent.set_right(green)
            self.root = node
            node.parent = node
        self.adjust_height(grand_parent)
        self.adjust_height(parent)
        self.adjust_height(node)
        if node.parent != node:
            self.splay(node)

        # Repeat the splay on node, if it is not the root yet, until it becomes the root.
    
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

def split_splay(tree, value):
    element_to_delete = tree._search(value)
    tree.splay(element_to_delete)
    if element_to_delete.key < value:
        right = BinarySearchTree(element_to_delete.right)
        element_to_delete.set_right(None)
        left = BinarySearchTree(element_to_delete)
        return (left, right)
    if element_to_delete.key > value:
        left = BinarySearchTree(element_to_delete.left)
        element_to_delete.set_left(None)
        right = BinarySearchTree(element_to_delete)
        return (left, right)
    if element_to_delete.key == value:
        left = BinarySearchTree(element_to_delete.left)
        right = BinarySearchTree(element_to_delete.right)
        return (left, right)

def merge_splay(tree1, tree2):
    n = tree1._search(float('inf'))
    tree1.splay(n)
    n.set_right(tree2.root)
    return tree1

#Tree 1
# tree1 = BinarySearchTree(Node(1))
# inserted = tree1.insert(2)
# inserted = tree1.insert(3)
# inserted = tree1.insert(4)
# inserted = tree1.insert(5)
# tree2 = BinarySearchTree(Node(10))
# inserted = tree2.insert(20)
# inserted = tree2.insert(30)
# inserted = tree2.insert(40)
# inserted = tree2.insert(50)

# print(tree1)
# print(tree2)
# tree3 = merge_avl(tree1, tree2)
# print(tree3)
# print("Splay 10")
# tree3.splay(tree3.search(10))
# tree3.splay(tree3.search(1))
# print(tree3)

# Tree2 Testing split
tree2 = BinarySearchTree(3)
tree2.insert(1)
tree2.insert(2)
print(tree2)
print(tree2._search(3).next())
print(tree2)
tree_left, tree_right = split_splay(tree2, 1.5)
print(tree_left)
print(tree_right)

# Tree3 and Tree4 testing merge
tree3 = BinarySearchTree(1)
tree3.insert(2)
tree3.insert(3)

tree4 = BinarySearchTree(10)
tree4.insert(20)
tree4.insert(30)

merged_tree = merge_splay(tree3, tree4)
print(merged_tree)