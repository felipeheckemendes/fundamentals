import random
def quick_sort(arr, lower, upper):
    if lower >= upper:
        return

    pivot_index = 0
    i = j = lower+1
    while i <= upper:
        if arr[i] <= arr[lower]:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
        i += 1
    arr[j-1], arr[lower] = arr[lower], arr[j-1]
    pivot_index = j-1

    quick_sort(arr, lower, pivot_index-1)
    quick_sort(arr, pivot_index+1, upper)
    return arr

def quick_sort_random(arr, lower, upper):
    if lower >= upper:
        return

    pivot_index = random.randint(lower, upper)
    arr[lower], arr[pivot_index] = arr[pivot_index], arr[lower]
    i = j = lower+1
    while i <= upper:
        if arr[i] <= arr[lower]:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
        i += 1
    arr[j-1], arr[lower] = arr[lower], arr[j-1]
    pivot_index = j-1

    quick_sort(arr, lower, pivot_index-1)
    quick_sort(arr, pivot_index+1, upper)
    return arr

print(quick_sort([6, 4, 6, 9, 5, 3, 9, 1, 9, 7], 0, 9))
print(quick_sort_random([6, 4, 6, 9, 5, 3, 9, 1, 9, 7], 0, 9))