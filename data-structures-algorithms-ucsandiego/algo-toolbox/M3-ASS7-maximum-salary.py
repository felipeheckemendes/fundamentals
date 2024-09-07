"""
Largest Concatenate Problem
Compile the largest integer by concatenating the given integers.
Input: A sequence of positive integers.
Output: The largest integer that can be obtained by concatenating the given integers in some order.
"""

def select_best_first(n, list):
    largest_digit = '0'
    selection = []

    if len(list) <= 1:
        return list[0]

    # Get all elements starting with the largest digit
    for element in list:
        # print(type(largest_digit), largest_digit)
        # print(type(element[1][0]), element[1][0], element[1], element)
        if element[1][0] == largest_digit:
            selection.append(element)
        elif element[1][0] > largest_digit:
            largest_digit = element[1][0]
            selection = []
            selection.append(element)
    # Remove the first digit (if only 1 digit, next digit = first) and select all elements with the highest first digit.
    for element in selection:
        if len(element[1]) == 1:
            pass
        else:
            # print("==", element[1][1:] )
            element[1] = element[1][1:]
    return select_best_first(len(selection), selection)

def largest_concatenate(n, list):
    if len(list) <= 1:
        print("YAYYYYY")
        return [list[0][0]]

    selected = select_best_first(n, list)
    list.remove(selected)
    return [selected[0]] + largest_concatenate(len(list), list)


    # Repeat until only 1 element left to choose, or elements are equal. Choose element, remove from list, and start again.
        
        

mylist = [[index, element] for index, element in enumerate(mylist)]
mylist = ['77', '96', '944', '9', '89']
print(mylist)
print(largest_concatenate(len(mylist), mylist))