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
    def __init__(self, root_key):
        self.root = Node(root_key)
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


    def adjust_height(self, node):
        # if node.key == 1:
        #     print("We are adjusting height of node 1")
        left_height = 0 if node.left == None else node.left.height
        right_height = 0 if node.right == None else node.right.height
        node.height = 1 + max(left_height, right_height)
        # if node.key == 1:
        #     print(left_height, right_height)
        #     print(node.height)

    def rebalance_right(self, node):
        if node.key == 5:
            print("Rebalancing right on node 5")
        node_a = node.left
        node_a_left_height = 0 if node_a.left == None else node_a.left.height
        node_a_right_height = 0 if node_a.right == None else node_a.right.height
        if node_a_right_height > node_a_left_height:
            self.rotate_left(node_a)
            self.adjust_height(node_a)
            self.adjust_height(node_a.parent)
        self.rotate_right(node)
        self.adjust_height(node)
        self.adjust_height(node.parent)

    def rebalance_left(self, node):
        node_a = node.right
        node_a_left_height = 0 if node_a.left == None else node_a.left.height
        node_a_right_height = 0 if node_a.right == None else node_a.right.height
        if node_a_left_height > node_a_right_height:
            self.rotate_right(node_a)
            self.adjust_height(node_a)
            self.adjust_height(node_a.parent)
        self.rotate_left(node)
        self.adjust_height(node)
        self.adjust_height(node.parent)

    def rebalance(self, node):
        parent = node.parent
        left_height = 0 if node.left == None else node.left.height
        right_height = 0 if node.right == None else node.right.height
        if left_height > right_height + 1:
            self.rebalance_right(node)
        elif right_height > left_height + 1:
            self.rebalance_left(node)
        self.adjust_height(node)
        if parent != node:
            self.rebalance(parent)

    def insert(self, key):
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
        print("Adding element", key)
        print(self)
        print("Rebalancing new node")
        self.rebalance(new_node)
        print(self)
        return new_node
    

    def remove_key(self, key):
        element_to_delete = self.search(key, self.root)
        if element_to_delete.key != key:
            return
        else:
            self.delete(element_to_delete)

    def delete(self, element_to_delete):
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
            if right != None:
                if element_to_delete == parent.left:
                    parent.set_left(right)
                if element_to_delete == parent.right:
                    parent.set_right(right)
                if element_to_delete == parent:
                    self.root = right
                    right.parent = right
                    parent = next_element
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
            self.adjust_height(next_element)

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

#Tree 1
tree = BinarySearchTree(5)
inserted = tree.insert(0)
inserted = tree.insert(1)
inserted = tree.insert(2)
inserted = tree.insert(3)
inserted = tree.insert(4)
inserted = tree.insert(6)
print(tree)
inserted = tree.insert(6)
inserted = tree.insert(6)
inserted = tree.insert(6)
print(tree)