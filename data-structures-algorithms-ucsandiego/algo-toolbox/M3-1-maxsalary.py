# Given certain digits (numbers from 0 to 9), find the highest salary that can be composed with it

def remove_highest_digit(string, toberemoved):
    # Find the index of the first digit
    # index = len(s)  # Default to length of string if no digit found
    for i, char in enumerate(string):
        if char == toberemoved:
            index = i
            break

    # Return the string without the first digit
    return string[:index] + string[index+1:]

def max_salary(digitstring):
    salary = ''
    max = 0

    while len(digitstring) > 0:
        # Find max
        max = 0
        for digit in digitstring:
            if int(digit) > int(max):
                max = digit    
        # Append max to salary list
        salary = salary + max

        # Remove from digit list
        digitstring = remove_highest_digit(digitstring, max)

    return salary

def max_salary_iterative(digitstring):
    # Base case
    if len(digitstring) == 1:
        return digitstring

    # Find max
    max = 0
    for digit in digitstring:
        if int(digit) > int(max):
            max = digit

    # Remove max from digitlist
    digitstring = remove_first_digit(digitstring, max)

    # Append max to salary string, and repeat for next ones
    salary = max + max_salary_iterative(digitstring)
    return salary

digitstring = input()
print(max_salary(digitstring))
        
