# Given n children at a party, each with different age, what are the groups of age that should be arranged so that we have children with at 
# most 2 years of difference of age on each group, but the number of groups is minimal

def groups_age_ranges(children_ages):
    index = 0
    ages = []
    while index < len(children_ages):
        group = [children_ages[index], children_ages[index]+2]
        ages.append(group)
        index = index+1
        while index < len(children_ages) and children_ages[index] <= group[1]:
            index = index + 1
    return ages

print(groups_age_ranges([1, 2, 7, 7, 7, 8, 9, 10, 11]))

def groups_age_ranges2(children_ages):
    
    ages = []
    #Start the first group at the first element on the array
    group = [children_ages[0], children_ages[0]+2]
    ages.append(group)

    for index, age in enumerate(children_ages):
        if age <= group[1]:
            pass
        else:
            group = [children_ages[index], children_ages[index]+2]
            ages.append(group)
    return ages

print(groups_age_ranges2([1, 2, 7, 7, 7, 8, 9, 10, 11]))