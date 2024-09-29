# Several patients arrive at a doctor at the same time.
# Each has his treatment time know beforehand.
# Determine the order in which to accept the patients so that total waiting time aggregate between all patients is the least.

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