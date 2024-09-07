"""
Cooking a Dinner Problem
Given an array that describes time it takes to cook each of n dishes and an array that describes how long the dishes stay fresh, 
is there an order of cooking these dishes that ensures that at some point all of them are fresh?

Input: You are cooking n dishes for a dinner. For the i-th dish, it takes ci minutes to cook it, after which it stays fresh for fi minutes.
Output: Is there an order of cooking these n dishes that ensures that at some point all of them are fresh? Assume that you cook them one by one and cannot parallelize your work.
"""

# Rationale for solution:
# The rationale is that it is possible to have all fresh only if for some dish, the Sum(preparing times) <= Dish(preparing time) + Dish(fresh time)
# If any such dish exists, it should obviously be prepared first.
# After selecting this as first dish, we repeat the same process for the remaining list of dishes, until we get to only one dish.


def cooking_order(dishes):
    
    if len(dishes) == 1:
        return dishes
    
    serving_order = []
    candidate = []

    # While there are still dishes to be prepared
    while len(dishes) > 0:
        
        candidate = None
        # Calculate time of preparation
        sum_preparing_times = 0
        for dish in dishes:
            sum_preparing_times = sum_preparing_times + dish[0]

        print("preparing time", sum_preparing_times)
        # Find a greedy object
        for index, dish in enumerate(dishes):
            if dish[0]+dish[1] > sum_preparing_times:
                print("Chosen dish total time", dish[0]+dish[1], dish[0], dish[1])
                candidate = index
        
        # If no solution is found, return that there is no solution
        if candidate == None:
            return None
            
        # Remove this from initial problem to reduce the problem
        # And add it to solution
        serving_order.append(dishes[candidate])
        print("Serving order ", serving_order, "\n")
        dishes.pop(candidate)


    # If all dishes were included on the preparation oreder, return the serving_order
    return serving_order
    

print(cooking_order([[6, 12],[5, 11],[5, 13],[3, 8]]))

