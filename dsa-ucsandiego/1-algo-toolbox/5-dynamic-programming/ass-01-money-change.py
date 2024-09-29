"""PROBLEM
5.2.1 Money Change Again
Money Change Again Problem
Compute the minimum number of coins needed To change the given value into coins with denominations 1, 3, and 4.
Input: An integer money.
Output: The minimum number of coins with denominations 1, 3, and 4 that changes money.
Input format. Integer money.
Output format. The minimum number of coins with denominations 1, 3, and 4 that changes money.
Constraints. 1 ≤ money ≤ 10**3
.
"""
def minimum_change(target, coins):
    minimum_coins_required = [0]
    
    for target in range(1, target+1):
        previous_coins = []
        for coin in coins:
            if target - coin >= 0:
                previous_coins.append(minimum_coins_required[target-coin])
        if previous_coins:
            minimum_coins_required.append(min(previous_coins) + 1)
        else:
            minimum_coins_required.append(float('inf')) # No possible combination of coins
    return minimum_coins_required[target]

money = int(input())
print(minimum_change(money, [1, 3, 4]))