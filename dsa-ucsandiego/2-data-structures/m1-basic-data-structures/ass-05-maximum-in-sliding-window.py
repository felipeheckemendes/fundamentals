"""PROBLEM
5 Maximum in Sliding Window
Problem Introduction
Given a sequence 𝑎1, . . . , 𝑎𝑛 of integers and an integer 𝑚 ≤ 𝑛, find the maximum among {𝑎𝑖, . . . , 𝑎𝑖+𝑚−1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1. 
A naive 𝑂(𝑛𝑚) algorithm for solving this problem scans each window separately.
Your goal is to design an 𝑂(𝑛) algorithm.
Problem Description
Input Format. The first line contains an integer 𝑛, the second line contains 𝑛 integers 𝑎1, . . . , 𝑎𝑛 separated by spaces, the third line contains an integer 𝑚.
Constraints. 1 ≤ 𝑛 ≤ 10**5, 1 ≤ 𝑚 ≤ 𝑛, 0 ≤ 𝑎𝑖 ≤ 10**5 for all 1 ≤ 𝑖 ≤ 𝑛.
Output Format. Output max{𝑎𝑖, . . . , 𝑎𝑖+𝑚−1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1.
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.max = value
        self.next = next

    def __str__(self):
        if self == None:
            return 'None'
        string = str(self.value) + ' -| '
        return string

class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        new_node = Node(value, self.top)
        if self.top != None and value > self.top.max:
            new_node.max = value
        elif self.top != None:
            new_node.max = self.top.max
        self.top = new_node

    def get_top(self):
        return self.top.value

    def get_max(self):
        return self.top.max

    def pop(self):
        if self.top == None:
            print("Error, empty stack")
            return
        popped = self.top
        self.top = self.top.next
        return popped.value
    
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False
    
    def __str__(self):
        string = 'out'
        current_node = self.top
        while current_node != None:
            string += '[' + str(current_node.value) + ', ' + str(current_node.max) + ']'
            current_node = current_node.next
        string += 'in'
        return string

def get_max_of_windows(arr, window_size):
    back = Stack()
    front = Stack()
    maxs = []

    for i in range(window_size):
        back.push(arr[i])
    i += 1

    while i < len(arr):
        # Move all the back to the front
        while not back.is_empty():
            front.push(back.pop())

        # Move the window forward by popping front and pushing a new on the back, until the front is empty
        while not front.is_empty() and i < len(arr):
            maxs.append(max(front.get_max() if not front.is_empty() else float('-inf'), back.get_max() if not back.is_empty() else float('-inf')))
            front.pop()
            back.push(arr[i])
            i += 1
        
    maxs.append(max(front.get_max() if not front.is_empty() else float('-inf'), back.get_max() if not back.is_empty() else float('-inf')))
    return maxs

n = int(input())
arr = list(map(int, input().split()[:n]))
m = int(input())

print(' '.join(map(str, get_max_of_windows(arr, m))))
