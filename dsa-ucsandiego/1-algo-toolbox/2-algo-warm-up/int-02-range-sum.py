# Given an integer array and a set of ranges in it, compute the sum for each range.

def rangecompute(array, start, end):
    sum = 0
    for i in range(start, end+1):
        sum = sum + array[i]
    return sum

arr = input().split()
arr = [int(element) for element in arr]
print(arr)
start, end = map(int, input().split())
print(rangecompute(arr, start, end))