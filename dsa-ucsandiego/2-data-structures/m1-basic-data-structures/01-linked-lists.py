class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        if self == None:
            return 'None'
        string = str(self.value) + ' -> '
        return string

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def push_front(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.tail == None:
            self.tail = self.head

    def top_front(self):
        return self.head.value

    def pop_front(self):
        if self.head == None:
            print("Error, empty list")
            return
        if self.tail == self.head:
            self.tail == None
        self.head = self.head.next
    
    def push_back(self, value):
        new_node = Node(value)
        if self.tail == None:  
            self.head = self.tail = new_node
        else:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            last_node.next = new_node
            self.tail = new_node
    
    def top_back(self):
        return self.tail.value

    def pop_back(self):
        if self.head == None:
            print("Error: empty list")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            before_last = self.head
            while before_last.next.next != None:
                before_last = before_last.next
            before_last.next = None
            self.tail = before_last


    def find_key(self, value):
        current_node = self.head
        while current_node != None and current_node.value != value:
            current_node = current_node.next
        return current_node
    
    def erase_key(self, value):
        if self.head == None:
            print("Error, empty list")
            return
        if self.head == self.tail and self.head.value == value:
            self.head = self.tail = None
            return
        
        previous_node = self.head
        while previous_node.next != None and previous_node.next.value != value:
             previous_node = previous_node.next
        previous_node.next = previous_node.next.next
    
    def is_empty(self):
        if self.head == self.tail == None:
            return True
        else:
            return False
    
    def __str__(self):
        string = 'head-> '
        current_node = self.head
        while current_node != None:
            string += str(current_node.value) + " -> "
            current_node = current_node.next
        string += 'null'
        return string


# Testing
mylist = LinkedList()
mylist.push_front(1)
mylist.push_front(2)
mylist.push_front(3)
mylist.push_front(4)
mylist.push_front(5)
print("List initialized: ",mylist)
print("Top front:", mylist.top_front())
mylist.pop_front()
print("Pop front:", mylist)
mylist.push_back(0)
print("Push back 0:", mylist)
print("Top back:", mylist.top_back())
mylist.pop_back()
print("Pop back:", mylist)
print("Find key 3:", mylist.find_key(3))
print("Find key 9:", mylist.find_key(9))
mylist.erase_key(2)
print("Erase key 2:", mylist)
print(mylist.is_empty())
mylist.pop_back()
mylist.pop_back()
print(mylist)
mylist.erase_key(4)
print("Pop back all:", mylist)
mylist.push_back(1)
mylist.push_back(2)
print("List initialized: ",mylist)
mylist.pop_front()
mylist.pop_front()
print("Pop front all:", mylist)