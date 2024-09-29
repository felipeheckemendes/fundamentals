# Given a list of loot with weight and value, fill a backpack of max weight with most valuable possible choices


def max_loot(max_weight, loot_items):
    remaining = max_weight
    looted_value =  0
    for _ in loot_items:
        item_to_take = loot_items[best_item(loot_items)]
        if remaining > item_to_take[1]:
            looted_value +=  item_to_take[0]
            remaining = remaining - item_to_take[1]
            item_to_take[0] = 0
            item_to_take[1] = 0
        if remaining <= item_to_take[1]:
            looted_value += item_to_take[0]/item_to_take[1]*remaining
            item_to_take[0] -= item_to_take[0]/item_to_take[1]*remaining
            item_to_take[1] -= remaining
            remaining = 0
    return looted_value

def best_item(loot_items):
    best_index = 0
    best_value = 0
    for index, item in enumerate(loot_items):
        if item[1] > 0 and item[0]/item[1] > best_value:
            best_index = index
            best_value = item[0]/item[1]
    return best_index

no_items, capacity = input().split()
no_items = int(no_items)
capacity = int(capacity)
products = []
for i in range(no_items):
    products.append(list(map(int, input().split())))

print(max_loot(capacity, products))
