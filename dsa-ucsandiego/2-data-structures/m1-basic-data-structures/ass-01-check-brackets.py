"""PROBLEM
1 Check brackets in the code
Problem Introduction
In this problem you will implement a feature for a text editor to find errors in the usage of brackets in the code.

Input Format. Input contains one string str which consists of big and small latin letters, digits, punctuation marks and brackets from the set []{}().
Output Format. If the code in str uses brackets correctly, output “Success" (without the quotes). 
Otherwise, output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing brackets, output the 1-based index of the first unmatched opening bracket.
"""
"""SOLUTION
Use a stack to store all opened brackets. For each closing bracket, check if it matches the opening in the top of the stack.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        if self == None:
            return 'None'
        string = str(self.value)
        return string

class Stack:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def push(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.tail == None:
            self.tail = self.head

    def top(self):
        return self.head.value

    def pop(self):
        if self.head == None:
            print("Error, empty stack")
            return
        if self.head == self.tail:
            self.tail = None
        popped = self.head
        self.head = self.head.next
        return popped.value
    
    def is_empty(self):
        if self.head == self.tail == None:
            return True
        else:
            return False
    
    def __str__(self):
        string = 'top'
        current_node = self.head
        while current_node != None:
            string += ' -> ' + str(current_node.value)
            current_node = current_node.next
        string += ' -> bottom'
        return string

def check_brackets(string):
    opening_stack = Stack()
    matches = {'(': ')', '[': ']', '{': '}'}

    for index, character in enumerate(string):
        if character == '[' or character == '(' or character == '{':
            opening_stack.push((character, index))
        elif character == ']' or character == ')' or character == '}':
            if matches[opening_stack.top()[0]] == character:
                opening_stack.pop()
            else:
                return index + 1
    if opening_stack.is_empty():
        return "Success"
    else:
        return opening_stack.top()[1] + 1

string = input()
print(check_brackets(string))
