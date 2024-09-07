"""
Minimum Unchangeable Amount Problem
Given a set of coins, find the minimum amount that cannot be changed using these coins

Input: Coins with denominations:
c1 ≤ c2 ≤ ··· ≤ cn.
Output: The minimum amount that cannot be changed using these n coins

"""

# SOLUTION
# In order to solve this, I use a list where changeable ammounts will be stored.
# Add the first/next coin to the list of changeable ammounts
# Add the sum of this coin with other changeable ammounts to the changeable ammounts -> To implement this it was necessary a temp list. Also, in order not to duplicate ammounts, a for loop to check if value was already on the list.
# Loop through the changeable list and check if missing any integer between 1 and max(changeable). If yes, return this value.
# 


def minimum_unchangeable(coins):
    changeable = []
    minimum_checked = 0
    
    coins.sort()
    for index, coin in enumerate(coins):
        print("Adding coin:", coin)
        changeable.append(coin)
        temp = []
        for index, value in enumerate(changeable[:-1]):
            temp.append(value+coin)
        for item in temp:
            if item not in changeable:
                changeable += [item]
        print(temp, changeable)
        for i in range(1, max(changeable)):
            if i not in changeable:
                return i
    return None

print(minimum_unchangeable([1, 2, 4, 10, 10]))


