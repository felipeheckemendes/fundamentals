def selection_sort(list):
    minimum_index = 0
    for i in range(len(list)):
        minimum_index = i
        for j in range(i, len(list)):
            if list[j] < list[minimum_index]:
                minimum_index = j
        list[i], list[minimum_index] = list[minimum_index], list[i]
    return list

print(selection_sort([-1, -2, -3, -4, -5]))

    