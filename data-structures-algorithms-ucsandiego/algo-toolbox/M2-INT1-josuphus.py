#  Given the Josephus problem: n people stand in a circle, every kth person dies. Which one survives

def josephus(n, k):
    # Returns the survivor index
    alive = list(range(n))
    n_alive = n
    print(alive)
    dead = []
    current = 0
    should_die = k - 1
    while n_alive>0:
        current = current % n
        if alive[current] == None:
            current += 1
            continue
        if should_die == 0:
            print("killing", current)
            alive[current] = None
            n_alive -= 1
            current += 1
            should_die = k - 1
            # dead.append(current)
        else:
            print("passing by", current)
            current += 1
            should_die = should_die - 1
        print("Alive", alive, "\n")
        # print("Dead", dead, "\n")
    return current - 1

def josephus2(n, k):
    alive = list(range(n))
    current = 0
    should_die = k - 1

    while len(alive)>1:

        # If we went further than last element (current == length), start on first element of list (index 0)
        if current == len(alive):
            current = 0
        if should_die == 0:
            alive.pop(current)
            should_die = k - 1
        else:
            current += 1
            should_die -= 1
        print(alive)
    return alive[0]

def josephus3(n, k):
    result = 0  # Base case: josephus(1, k) is 0
    for i in range(2, n + 1):
        result = (result + k) % i
    return result


def josephus4(n, k):
    # Outer loop, loops through remaining prisoners
    alive = list(range(n))
    current = 0
    while len(alive)>1:
        print(current, alive)
        # Ineer loop, loops through the kill counter 
        for i in range(k):
            if current == len(alive):
                current = 0
            if i == k-1:
                alive.pop(current)
            else:
                current += 1
    return alive

print(josephus2(10, 2))

