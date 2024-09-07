# Given an integer array and a set of ranges in it, compute the sum for each range.

def rangecompute(array, start, end):
    sum = 0
    for i in range(start, end):
        sum = sum + array[i]
    return sum

arr = [1,2,3,4,5]
print(
    rangecompute(arr, 1, 1)
)