#  Given the Josephus problem: n people stand in a circle, every kth person dies. Which one survives

def josephus(n, k):
    """
    This solution is good in that it does not use the pop method, which takes n time.
    However, it does not reduce the list, and so it loops through the list total ~k times.
    Either way, this k times only makes the complexity k*n.
    """
    # Returns the survivor index
    alive = list(range(n))
    n_alive = n
    current = 0
    should_die = k - 1
    while n_alive>0:
        current = current % n
        if alive[current] == None:
            current += 1
            continue
        if should_die == 0:
            alive[current] = None
            n_alive -= 1
            current += 1
            should_die = k - 1
        else:
            current += 1
            should_die = should_die - 1
    return current - 1

def josephus2(n, k):
    """
    Relies on the pop method, which takes n time in the worst case.
    For this reason, complexity can be n^2.
    If using linked lists on this method, complexity would be reduced to n.
    """
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
    """
    Most elegant solution.
    Does not rely on the pop, which takes extra time to solve.
    Complexity n.
    """
    result = 0  # Base case: josephus(1, k) is 0
    for i in range(2, n + 1):
        result = (result + k) % i
    return result


def josephus4(n, k):
    """
    Also uses pop method. Could reduce complexity to n if implemented using linked lists.
    """
    alive = list(range(n))
    current = 0
    # Outer loop, loops through remaining prisoners
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

n, k = map(int, input().split())
print(josephus(n, k))

