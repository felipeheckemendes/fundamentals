"""
We will rely on a lemma
If r is the remainder of a / b
gcd of "a" and "b" = gcd of "r" and "b"

"""

def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

a, b = map(int, input().split())

print(gcd(a, b))