class Node:
    def __init__(self, key, parent):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
    
    # def __str__(self):
    #     return str(self.key)

    def next(self):
        # # if self.right == None and self.left == None and self.parent.key < self.key:
        # if self.parent == None:
        #     return None
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
        if self.parent.key > self.key:
            return self.parent
        elif self.parent.key < self.key:
            return self.parent.right_ancestor()
        elif self.parent.key == self.key or self.parent.key == None:
            return None


    def __str__(self):
        # Start the string representation from the root node.
        return str(self.key)

    
class BinarySearchTree:
    def __init__(self, root_key):
        self.root = Node(root_key, None)
        self.root.parent = self.root

    def search(self, value, root):
        if root.key == value:
            return root
        elif root.key > value:
            if root.left == None:
                return root
            else:
                return self.search(value, root.left)
        elif root.key < value:
            if root.right == None:
                return root
            else:
                return self.search(value, root.right)

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

    def insert(self, key):
        target = self.search(key, self.root)
        if target.key >= key:
            if target.left == None:
                new_node = Node(key, target)
                target.left = new_node
            else:
                new_node = Node(key, target)
                target.left.parent = new_node
                new_node.left = target.left
                new_node.right = target.left.right
                if new_node.right != None:
                    new_node.right.parent = new_node
                target.left = new_node
        elif target.key < key:
            if target.right == None:
                new_node = Node(key, target)
                target.right = new_node
            else:
                new_node = Node(key, target)
                target.right.parent = new_node
                new_node.right = target.right
                new_node.left = target.right.left
                if new_node.left != None:
                    new_node.left.parent = new_node
                target.right = new_node
        return new_node

    def remove_key(self, key):
        element_to_delete = self.search(key, self.root)
        if element_to_delete.key != key:
            return
        else:
            self.delete(element_to_delete)

    def delete(self, element_to_delete):
        if element_to_delete.right == None:
            if element_to_delete == element_to_delete.parent.left:
                element_to_delete.parent.left = element_to_delete.left
                element_to_delete.left.parent = element_to_delete.parent
            if element_to_delete == element_to_delete.parent.right:
                element_to_delete.parent.right = element_to_delete.left
                element_to_delete.left.parent = element_to_delete.parent
        else:
            next_element = element_to_delete.next()
            if element_to_delete == element_to_delete.parent.left:
                element_to_delete.parent.left = next_element
                # Promote next element's right element
                next_element.parent.left = next_element.right
                next_element.right.parent = next_element.parent
                
                next_element.right = element_to_delete.right
                element_to_delete.right.parent = next_element
                next_element.parent = element_to_delete.parent
            if element_to_delete == element_to_delete.parent.right:
                element_to_delete.parent.right = next_element
                # Promote next element's right element
                next_element.parent.left = next_element.right
                next_element.right.parent = next_element.parent

                next_element.right = element_to_delete.right
                element_to_delete.right.parent = next_element
                next_element.parent = element_to_delete.parent

    def __str__(self):
        # Start the string representation from the root node.
        return self._str_helper(self.root, 0)

    def _str_helper(self, node, level):
        # Base case: if the node is None, return an empty string
        if node is None:
            return ""
        
        # Prepare the indentation for the current level
        indent = "  " * level
        result = f"{indent}{node.key}\n"

        # Recursively call for the left and right children
        result += self._str_helper(node.left, level + 1)  # Left subtree with increased level
        result += self._str_helper(node.right, level + 1)  # Right subtree with increased level

        return result


#Tree 1
tree = BinarySearchTree(5)
node3 = Node(3, tree.root)
node4 = Node(4, node3)
node2 = Node(2, node3)
node1 = Node(1, node2)

node7 = Node(7, tree.root)
node6 = Node(6, node7)
node8 = Node(8, node7)
node9 = Node(9, node8)

tree.root.left = node3
node3.right = node4
node3.left = node2
node2.left = node1

tree.root.right = node7
node7.left = node6
node7.right = node8
node8.right = node9

#Tree 2
# tree= BinarySearchTree(7)
# node4 = Node(4, tree.root)
# tree.root.left = node4
# node1 = Node(1, node4)
# node4.left = node1
# node6 = Node(6, node4)
# node4.right = node6

# node13 = Node(13, tree.root)
# tree.root.right = node13
# node10 = Node(10, node13)
# node13.left = node10
# node15 = Node(15, node13)
# node13.right = node15

print("Adding and removing element with key 3")
print(tree)
inserted = tree.insert(3)
print(tree)
tree.delete(inserted)
print(tree)
print()

print("Searching for element with key 5")
print(tree.search(5, tree.root))
print()

print("Range search from 2 to 5")
range_elements = tree.range_search(2, 5)
for element in range_elements:
    print(element.key)
