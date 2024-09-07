"""
Job Scheduling Problem
Given an array of jobs, where each job is associated with its profit and deadline, find an ordering of all jobs that maximizes the profit. A job
generates a profit only if it is completed before
the deadline.

Input: An array of jobs, where each job Job is associated with its profit (denoted as profit(Job)) and deadline (denoted as deadline(Job)). 
Each job takes a single unit of time and no two jobs can be performed at the same time.
Given an ordering of all jobs, we say that the i-th job Job in this ordering is well-scheduled if i ≤ deadline(Job), i.e., if it is finished before the deadline.
The profit of this ordering is defined as the total profit of all well-scheduled jobs. 
We assume that the first job starts at time 0. 
Output: Ordering of all jobs that maximizes the profit among all possible orderings.
"""

def job_scheduling(jobs):
    ordered_jobs = selection_sort(jobs)
    schedule = []
    unscheduled = []
    profit = 0
    for _ in jobs:
        schedule.append(None)

    for job in ordered_jobs:
        position = job[1]-1
        while position >= 0:
            if schedule[position] == None:
                schedule[position] = job
                break
            else:
                position -= 1
        if position < 0:
            unscheduled.append(job)

    for job in schedule:
        if job is not None:
            profit += job[0]
    
    for index, job in enumerate(unscheduled):
        if schedule[-index-1] == None:
            schedule[-index-1] = job

    return [profit, schedule]
        

def selection_sort(jobs):
    if len(jobs)<=1:
        return jobs
    greater_than_pivot = []
    lesser_than_pivot = []
    pivot = jobs[0]

    for job in jobs[1:]:
        if job[0] > pivot[0]:
            greater_than_pivot.append(job)
        elif job[0] <= pivot[0]:
            lesser_than_pivot.append(job)
    return selection_sort(greater_than_pivot) + [pivot] + selection_sort(lesser_than_pivot)



jobs = [[500, 2], [400, 2], [10, 2], [5, 2]]
# First number -> Profit
# Second number -> deadline
print(job_scheduling(jobs))