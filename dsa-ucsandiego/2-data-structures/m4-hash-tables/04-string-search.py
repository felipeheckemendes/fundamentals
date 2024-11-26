import random

prime = 10000019 #Prime number needs to be bigger than the the largests phone number to be hashed. In our case, since telephone numbers have 7 digitis, it needs to be bigger than 9.999.999
x = random.randint(1, prime-1)

def hash(key):
    hashed_value = 0
    for letter in reversed(key):
        hashed_value = hashed_value*x + ord(letter)
        hashed_value = (hashed_value)%prime
    return hashed_value

def find_substring(string, substring):
    searched_hash = hash(substring)
    positions = []
    current_hash = hash(string[len(string)-len(substring):])
    for index in range(len(string)-len(substring), -1, -1):
        if index < len(string)-len(substring):
            current_hash = (x*current_hash + hash(string[index]) - hash(string[index+len(substring)])*x**(len(substring)) )%prime
        if current_hash == searched_hash:
            if string[index:index+len(substring)] == substring:
                positions.append(index)
    return positions

string = 'abcdabcd'
substring = 'abcd'
print(find_substring(string, substring))



