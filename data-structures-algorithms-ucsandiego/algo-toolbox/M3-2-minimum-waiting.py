# 

# My own proposition
def minimum_time(waiting_times):

    if len(waiting_times) <= 1:
        return 0

    minimum = waiting_times[0]
    minimum_index = 0
    for index, time in enumerate(waiting_times):
        if time < minimum:
            minimum = time
            minimum_index = index
    waiting_times.pop(minimum_index)
    total = minimum*len(waiting_times) + minimum_time(waiting_times)
    return total

print(minimum_time([10, 15, 20]))

# Class implementation
def waiting_time(waiting)