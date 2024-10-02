"""PROBLEM
3 Network packet processing simulation
Problem Introduction
In this problem you will implement a program to simulate the processing of network packets.
Problem Description
Task. You are given a series of incoming network packets, and your task is to simulate their processing.
Packets arrive in some order. For each packet number 𝑖, you know the time when it arrived 𝐴𝑖 and the
time it takes the processor to process it 𝑃𝑖 (both in milliseconds). There is only one processor, and it
processes the incoming packets in the order of their arrival. If the processor started to process some
packet, it doesn’t interrupt or stop until it finishes the processing of this packet, and the processing of
packet 𝑖 takes exactly 𝑃𝑖 milliseconds.
The computer processing the packets has a network buffer of fixed size 𝑆. When packets arrive,
they are stored in the buffer before being processed. However, if the buffer is full when a packet
arrives (there are 𝑆 packets which have arrived before this packet, and the computer hasn’t finished
processing any of them), it is dropped and won’t be processed at all. If several packets arrive at the
same time, they are first all stored in the buffer (some of them may be dropped because of that —
those which are described later in the input). The computer processes the packets in the order of
their arrival, and it starts processing the next available packet from the buffer as soon as it finishes
processing the previous one. If at some point the computer is not busy, and there are no packets in
the buffer, the computer just waits for the next packet to arrive. Note that a packet leaves the buffer
and frees the space in the buffer as soon as the computer finishes processing it.

Input Format. The first line of the input contains the size 𝑆 of the buffer and the number 𝑛 of incoming
network packets. Each of the next 𝑛 lines contains two numbers. 𝑖-th line contains the time of arrival
𝐴𝑖 and the processing time 𝑃𝑖 (both in milliseconds) of the 𝑖-th packet. It is guaranteed that the
sequence of arrival times is non-decreasing (however, it can contain the exact same times of arrival in
milliseconds — in this case the packet which is earlier in the input is considered to have arrived earlier).

Constraints. All the numbers in the input are integers. 1 ≤ 𝑆 ≤ 10**5; 0 ≤ 𝑛 ≤ 10**5; 0 ≤ 𝐴𝑖 ≤ 10**6;
0 ≤ 𝑃𝑖 ≤ 10**3; 𝐴𝑖 ≤ 𝐴𝑖+1 for 1 ≤ 𝑖 ≤ 𝑛 − 1.

Output Format. For each packet output either the moment of time (in milliseconds) when the processor
began processing it or −1 if the packet was dropped (output the answers for the packets in the same
order as the packets are given in the input).
"""
class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self):
        if self == None:
            return 'None'
        string = str(self.value) + ' -> '
        return string

class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, value):
        new_node = Node(value)
        if self.head != None:
            self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = self.head

    def top_front(self):
        return self.head.value   
    
    def top_back(self):
        return self.tail.value

    def dequeue(self):
        if self.tail == None:
            print("Error, empty list")
            return
        if self.head == self.tail:
            dequeued = self.tail
            self.head = self.tail = None
        else:
            dequeued = self.tail
            self.tail.previous.next = None
            self.tail = self.tail.previous
        return dequeued
    
    def is_empty(self):
        if self.head == self.tail == None:
            return True
        else:
            return False
    
    def __str__(self):
        string1 = 'In'
        current_node = self.head
        while current_node != None:
            string1 += ' -> ' + str(current_node.value)
            current_node = current_node.next
        string1 += ' -> Out'
        return string1

def process_packets(buffer_size, packets):
    if len(packets) == 0:
        return []

    incoming_queue = Queue()
    for item in packets:
        incoming_queue.enqueue(item)
    queue = Queue()    
    items_in_queue = 0
    current_time = 0
    processed_times = []

    while incoming_queue.is_empty() == False or queue.is_empty() == False:
        print(queue)
        while items_in_queue < buffer_size and not incoming_queue.is_empty():
            incoming = incoming_queue.dequeue()
            if current_time <= incoming.value[0]:
                queue.enqueue(incoming.value)
                items_in_queue += 1
            else:
                processed_times.append(-1)
        
        if not queue.is_empty():
            current = queue.dequeue()
            items_in_queue -= 1
            if current_time < current.value[0]:
                current_time = current.value[0]
            processed_times.append(current_time)
            current_time += current.value[1]

    return processed_times

buffer_size, no_packets = map(int, input().split())
packets = []
for i in range(no_packets):
    packet = list(map(int, input().split()))
    packets.append(packet)

result = process_packets(buffer_size, packets)
for element in result:
    print(element)