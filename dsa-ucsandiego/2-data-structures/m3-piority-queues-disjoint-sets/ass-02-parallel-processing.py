"""PROBLEM
Parallel processing
Problem Introduction
In this problem you will simulate a program that processes a list of jobs in parallel. Operating systems such
as Linux, MacOS or Windows all have special programs in them called schedulers which do exactly this with
the programs on your computer.

Problem Description
Task. You have a program which is parallelized and uses 𝑛 independent threads to process the given list of 𝑚
jobs. Threads take jobs in the order they are given in the input. If there is a free thread, it immediately
takes the next job from the list. If a thread has started processing a job, it doesn’t interrupt or stop
until it finishes processing the job. If several threads try to take jobs from the list simultaneously, the
thread with smaller index takes the job. For each job you know exactly how long will it take any thread
to process this job, and this time is the same for all the threads. You need to determine for each job
which thread will process it and when will it start processing.

Input Format. The first line of the input contains integers 𝑛 and 𝑚.
The second line contains 𝑚 integers 𝑡𝑖 — the times in seconds it takes any thread to process 𝑖-th job.
The times are given in the same order as they are in the list from which threads take jobs.
Threads are indexed starting from 0.

Constraints. 1 ≤ 𝑛 ≤ 10**5; 1 ≤ 𝑚 ≤ 10**5; 0 ≤ 𝑡𝑖 ≤ 10**9.

Output Format. Output exactly 𝑚 lines. 𝑖-th line (0-based index is used) should contain two spaceseparated
integers — the 0-based index of the thread which will process the 𝑖-th job and the time
in seconds when it will start processing that job.
"""
"""SOLUTION
We can create a minimum heap in order to track the jobs on the threads and which will be the first to finish among them.
Each time a job finishes, we add a new one. 
We need to keep track of the time.
One possible issue with my solution is that for each finished job, the algorithm goes through all elements currently on the heap to decrease their remaining time
"""
class PriorityQueue:
    def __init__(self, max_size=100, size=0):
        self.max_size = max_size
        self.size = size
        self.arr = [None]*max_size
    
    def is_full(self):
        if self.size >= self.max_size:
            return True
        else:
            return False

    def left_child_index(self, index):
        if (index + 1)*2-1 < self.size:
            return (index + 1)*2-1
        else:
            return index

    def right_child_index(self, index):
        if (index + 1)*2 < self.size:
            return (index + 1)*2
        else:
            return index

    def parent_index(self, index):
        if index > 0:
            return (index-1)//2
        else:
            return 0

    def swap(self, index1, index2):
        self.arr[index1], self.arr[index2] = self.arr[index2], self.arr[index1]

    def sift_up(self, index):
        parent = self.parent_index(index)
        while self.arr[parent][1] > self.arr[index][1]:
            self.swap(parent, index)
            index = parent
            parent = self.parent_index(index)

    def sift_down(self, index):
        left_child = self.left_child_index(index)
        right_child = self.right_child_index(index)
        while self.arr[left_child][1] < self.arr[index][1] or self.arr[right_child][1] < self.arr[index][1]:
            if self.arr[left_child][1] <= self.arr[right_child][1]:
                self.swap(left_child, index)
                index = left_child
                left_child = self.left_child_index(index)
                right_child = self.right_child_index(index)
            else:
                self.swap(right_child, index)
                index = right_child
                left_child = self.left_child_index(index)
                right_child = self.right_child_index(index)

    def min(self):
        return self.arr[0]

    def extract_min(self):
        if self.size <= 0:
            return "Error, no elements to remove"
        self.swap(0, self.size-1)
        self.size -= 1
        self.sift_down(0)
        return self.arr[self.size]
    
    def add_element(self, element):
        if self.size < self.max_size:
            self.arr[self.size] = element
            self.size += 1
            self.sift_up(self.size-1)
            return element
        else:
            print("ERROR, not possible to add", element, ":array full")


def process_jobs(no_threads, jobs_list):
    jobs = [[index, value] for index, value in enumerate(jobs_list)]
    index = 0
    processing = PriorityQueue(no_threads, 0)
    processing_result = [None for element in jobs] 
    time = 0

    while not processing.is_full() and index < len(jobs):
        processing.add_element(jobs[index] + [index] + [0])
        index += 1

    while index < len(jobs) or processing.size != 0:     
        job = processing.extract_min()
        job_index = job[0]
        job_time = job[1]
        job_thread = job[2]
        job_start = job[3]
        processing_result[job_index] = [job_thread, job_start]
        time += job_time

        for i in range(0, processing.size):
            processing.arr[i][1] -= job_time

        if index < len(jobs):
            added = processing.add_element(jobs[index] + [job_thread] + [time])
            index += 1

    return processing_result

n, m = map(int, input().split())
jobs = map(int, input().split()[:m])
result = process_jobs(n, jobs)
for element in result:
    print(str(element[0]) + ' ' + str(element[1]))