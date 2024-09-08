# Naive algorithm to compute the Greatest Common Divider GCD between two numbers a and b

def gcd_naive(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    min_value = min(a, b)
    
    for d in range (1, min_value + 1):
        if a % d == 0 and b % d == 0:
            gcd = d
    return gcd

a, b = input().split()
a, b = [int(a), int(b)]
print(gcd_naive(a, b))

# Not possible to compute:
# print(gcd_naive(49535164894516487561, 15468765431269784650))
