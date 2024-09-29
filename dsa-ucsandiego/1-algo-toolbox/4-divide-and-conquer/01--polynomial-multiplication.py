import math

def fill_pol(pol, length):
    if len(pol) < length:
        return [0 for _ in range(len(pol), length)] + pol
    else:
        return pol

def fill_pow2(pol):
    """
    Fills a polynomial list representation, so that the length is a power of 2
    """
    if not math.log(len(pol), 2) % 1 == 0:
        power = int(math.log(len(pol), 2) // 1 + 1)
        length = 2**power
        return fill_pol(pol, length)
    else:
        return pol

def equalize_length(a, b):
    length = max(len(a), len(b))
    a = fill_pol(a, length)
    b = fill_pol(b, length)
    return [a, b]

def pol_multiplication_naive(a, b):
    a, b = equalize_length(a, b)
    result = [0 for _ in range(len(a)*2-1)]
    for i in range(len(a)):
        for j in range(len(b)):
            result[i+j] += a[i]*b[j]
    return result

def pol_multiplication_divide(a, b):
    a = fill_pow2(a)
    b = fill_pow2(b)
    a, b = equalize_length(a, b)
    n = int(len(a))

    if n == 1:
        return [a[0]*b[0]]

    half = int(n/2)

    a1 = a[:half]
    a2 = a[half:]
    b1 = b[:half]
    b2 = b[half:]

    a1b1 = pol_multiplication_divide(a1, b1)
    a1b2 = pol_multiplication_divide(a1, b2)
    a2b1 = pol_multiplication_divide(a2, b1)
    a2b2 = pol_multiplication_divide(a2, b2)

    result1 = a1b1 
    result2 = [a1b2[i]+a2b1[i] for i in range(len(a1b2))]
    result3 = a2b2


    result = [0 for _ in range(len(a)*2-1)]


    for i in range(len(result1)):
        result[i] += result1[i]
    for i in range(len(result2)):
        result[i+len(result3)+1] += result3[i]
    for i in range(len(result2)):
        result[i+len(result2)//2+1] += result2[i]
    return result

def pol_multiplication_karatsuba(a, b):
    a = fill_pow2(a)
    b = fill_pow2(b)
    a, b = equalize_length(a, b)
    n = int(len(a))

    if n == 1:
        return [a[0]*b[0]]

    half = int(n/2)

    a1 = a[:half]
    a2 = a[half:]
    b1 = b[:half]
    b2 = b[half:]

    a1b1 = pol_multiplication_karatsuba(a1, b1)

    a2b2 = pol_multiplication_karatsuba(a2, b2)

    c1 = [a1[i]+a2[i] for i in range(len(a1))]
    c2 = [b1[i]+b2[i] for i in range(len(b1))]
    c1c2 = pol_multiplication_karatsuba(c1, c2)
    for i in range(len(c1c2)):
        c1c2[i] = c1c2[i] - a1b1[i] - a2b2[i]

    result1 = a1b1 
    result2 = c1c2
    result3 = a2b2


    result = [0 for _ in range(len(a)*2-1)]


    for i in range(len(result1)):
        result[i] += result1[i]
    for i in range(len(result2)):
        result[i+len(result3)+1] += result3[i]
    for i in range(len(result2)):
        result[i+len(result2)//2+1] += result2[i]
    
    return result



pol_a = [4, 3, 2, 1]
pol_b = [1, 2, 3, 4]

result = [4, 11, 20, 30, 20, 11, 4]

print(pol_multiplication_naive(pol_a, pol_b) == result)
print(pol_multiplication_divide(pol_a, pol_b) == result)
print(pol_multiplication_karatsuba(pol_a, pol_b) == result)

