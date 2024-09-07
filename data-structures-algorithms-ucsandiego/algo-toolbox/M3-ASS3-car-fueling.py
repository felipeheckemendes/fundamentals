"""
Compute the minimum number of gas tank refills to get from one city to another.

Input: Integers d and m, as well as a sequence of integers stop1 < stop2 < ··· < stopn.

Output: The minimum number of refills to get from one city to another if a car can travel at most m miles on a full tank.
The distance between the cities is d miles and there are gas stations at distances stop1, stop2,..., stopn along the way. 
We assume that a car starts with a full tank.
"""

# distance_between_cities = int(input("Distance between cities to travel: "))
# longest_distance_travel = int(input("Longest distance car can travel with a fuel tank: "))
# number_of_stations = int(input("Number of gas stations: "))
# gas_stations = [[] for gas_station in range(number_of_stations)]
# for index, _ in enumerate(gas_stations):
#     gas_stations[index] = input(f"Position of gas station nº {index+1}: ")

distance_between_cities = 950
longest_distance_travel = 450
number_of_stations = 4
gas_stations = [[] for gas_station in range(number_of_stations)]
gas_stations[0] = 200
gas_stations[1] = 375
gas_stations[2] = 550
gas_stations[3] = 750

def minimum_stops(distance_between_cities, longest_distance_travel, gas_stations):
    no_of_stops = 0
    car_position = 0
    new_car_position = 0
    while car_position < distance_between_cities - longest_distance_travel:
        for gas_station in gas_stations:
            if gas_station > car_position and gas_station < car_position + longest_distance_travel:
                new_car_position = gas_station
        if new_car_position == car_position:
            return -1
        elif new_car_position > car_position:
            car_position = new_car_position
            no_of_stops += 1
    return no_of_stops

print(minimum_stops(distance_between_cities, longest_distance_travel, gas_stations), "\n")

def minimum_stops_recursive(car_position, distance_between_cities, longest_distance_travel, gas_stations):
    
    if distance_between_cities - car_position <= longest_distance_travel:
        return 0
    
    stopped = None
    new_car_position = 0
    for gas_station in gas_stations:
        if gas_station <= car_position + longest_distance_travel:
            new_car_position = max(car_position, gas_station, new_car_position)
            stopped = True
    if stopped:
        car_position = new_car_position
        return 1 + minimum_stops_recursive(car_position, distance_between_cities, longest_distance_travel, gas_stations)
    else:
        return -1

print(minimum_stops_recursive(0, distance_between_cities, longest_distance_travel, gas_stations), "\n")
        
def minimum_stops2(distance_between_cities, longest_distance_travel, gas_stations):
    
    number_of_stops = 0
    car_position = 0
    while car_position <= distance_between_cities - longest_distance_travel:
        distance_to_travel = distance_to_max_reachable_stop(car_position, longest_distance_travel, gas_stations)
        if distance_to_travel > 0:
            car_position += distance_to_travel
            number_of_stops += 1
        else:
            return -1
    return number_of_stops

def distance_to_max_reachable_stop(car_position, longest_distance_travel, gas_stations):
    distance_to_travel = 0
    for gas_station in gas_stations:
        if gas_station <= car_position + longest_distance_travel and gas_station > car_position + distance_to_travel:
            distance_to_travel = gas_station - car_position
    return distance_to_travel

print(minimum_stops2(distance_between_cities, longest_distance_travel, gas_stations))
        

