import random
# no_calls1 = 0
# no_calls2 = 0
def quick_sort3p_1st(arr, lower, upper):
    """
    This first attemp version keeps the pivot on the lower position. Only at the end is it swapped with the m1-1 element.
    """
    # global no_calls1
    # no_calls1 += 1
    if lower>=upper:
        return arr

    m1, i, m2 = lower+1, lower+1, upper
    while i <= m2:
        if arr[i] < arr[lower]:
            arr[m1], arr[i] = arr[i], arr[m1]
            m1 += 1
            i += 1
        elif arr[i] == arr[lower]:
            i += 1
        elif arr[i] > arr[lower]:
            arr[i], arr[m2] = arr[m2], arr[i]
            m2 -= 1
    arr[lower], arr[m1-1] = arr[m1-1], arr[lower]
    m1 -= 1
    quick_sort3p_1st(arr, lower, m1-1)
    quick_sort3p_1st(arr, m2+1, upper)
    return arr


def quick_sort3p_2nd(arr, lower, upper):
    """
    This second attemp version moves the pivot up as it finds new elements lesser than the pivot. The code is cleaner, but it seems like slightly more calls are necessary.
    This code seems to be the more traditional implementation of quicksort 3 partitions.
    """
    # global no_calls2
    # no_calls2 += 1
    if lower>=upper:
        return arr

    m1, i, m2 = lower, lower+1, upper
    while i <= m2:
        if arr[i] < arr[m1]:
            arr[m1], arr[i] = arr[i], arr[m1]
            m1 += 1
            i += 1
        elif arr[i] == arr[m1]:
            i += 1
        elif arr[i] > arr[m1]:
            arr[i], arr[m2] = arr[m2], arr[i]
            m2 -= 1
    quick_sort3p_2nd(arr, lower, m1-1)
    quick_sort3p_2nd(arr, m2+1, upper)
    return arr

def quick_sort3p_random(arr, lower, upper):
    """
    This third version extends on the second version, adding an extra functionality of random pivots.
    """
    # global no_calls2
    # no_calls2 += 1
    if lower>=upper:
        return arr

    pivot_index = random.randint(lower, upper)
    arr[lower], arr[pivot_index] = arr[pivot_index], arr[lower]
    m1, i, m2 = lower, lower+1, upper
    while i <= m2:
        if arr[i] < arr[m1]:
            arr[m1], arr[i] = arr[i], arr[m1]
            m1 += 1
            i += 1
        elif arr[i] == arr[m1]:
            i += 1
        elif arr[i] > arr[m1]:
            arr[i], arr[m2] = arr[m2], arr[i]
            m2 -= 1
    quick_sort3p_random(arr, lower, m1-1)
    quick_sort3p_random(arr, m2+1, upper)
    return arr
    

print(quick_sort3p_1st([6, 4, 5, 6, 9, 5, 5, 5, 3, 9, 1, 9, 7], 0, 12))
print(quick_sort3p_2nd([6, 4, 5, 6, 9, 5, 5, 5, 3, 9, 1, 9, 7], 0, 12))
print(quick_sort3p_random([6, 4, 5, 6, 9, 5, 5, 5, 3, 9, 1, 9, 7], 0, 12))
# print(no_calls1, no_calls2)