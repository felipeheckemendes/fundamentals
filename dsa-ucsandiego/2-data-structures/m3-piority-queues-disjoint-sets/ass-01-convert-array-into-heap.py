
number_swaps = 0
swaps = []

def swap(arr, i, j):
    global number_swaps, swaps
    number_swaps += 1
    swaps.append(str(i) + ' ' + str(j))
    arr[i], arr[j] = arr[j], arr[i]

def left_child(arr, index):
    left_index = index*2 + 1
    if left_index < len(arr):
        return left_index
    else:
        return None

def right_child(arr, index):
    right_index = index*2 + 2
    if right_index < len(arr):
        return right_index
    else:
        return None

def parent(arr, index):
    parent_index = (index-1)//2
    return parent_index

def sift_down(arr, index):
    left = left_child(arr, index)
    right = right_child(arr, index)
    if right == None and left == None:
        return
    elif right == None:
        if arr[left] < arr[index]:
            swap(arr, index, left)
            print(index, left)
    elif arr[index] > arr[left] or arr[index] > arr[right]:
        if arr[left] < arr[right]:
            swap(arr, index, left)
            sift_down(arr, left)
        elif arr[left] > arr[right]:
            swap(arr, index, right)
            sift_down(arr, right)
    else:
        return

def convert_to_heap(arr):
    for index in range(len(arr)-1, -1, -1):
        sift_down(arr, index)
    return arr

n = int(input())
arr = list(map(int, input().split()[:n]))
convert_to_heap(arr)
print(number_swaps)
for swap in swaps:
    print(swap)