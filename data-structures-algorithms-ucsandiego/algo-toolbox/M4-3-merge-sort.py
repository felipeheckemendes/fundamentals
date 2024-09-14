def merge_sort(list):
    if len(list) <= 1:
        return list
    
    result, i, j = [], 0, 0
    left, right = merge_sort(list[:len(list)//2]), merge_sort(list[len(list)//2:])
    while i < len(left)  and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]

print(merge_sort([6, 5, 4, 3, 2, 1, 0]))