def fibonacci1(n):
    series = []
    if n >= 0:
        series.append(0)
    if n > 0:
        series.append(1)
    if n >= 1:
        for i in range(2, n+1):
            series.append(series[i-1]+series[i-2])
    return series[n]


def fibonacci2(n):
    fibonacci = 0
    for i in range(n+1):
        if i == 0:
            fibonacci = 0
            n_minus_2 = n_minus_1 = 0
        elif i == 1:
            fibonacci = 1
            n_minus_1 = 1
        else:
            fibonacci = n_minus_2 + n_minus_1
            n_minus_2 = n_minus_1
            n_minus_1 = fibonacci
    return fibonacci

# print(fibonacci2(0) == fibonacci1(0), fibonacci2(0), fibonacci1(0))
# print(fibonacci2(1) == fibonacci1(1), fibonacci2(1), fibonacci1(1))
# print(fibonacci2(2) == fibonacci1(2), fibonacci2(2), fibonacci1(2))
# print(fibonacci2(3) == fibonacci1(3), fibonacci2(3), fibonacci1(3))
# print(fibonacci2(4) == fibonacci1(4), fibonacci2(4), fibonacci1(4))
# print(fibonacci2(5) == fibonacci1(5), fibonacci2(5), fibonacci1(5))
# print(fibonacci2(6) == fibonacci1(6), fibonacci2(6), fibonacci1(6))
# print(fibonacci2(7) == fibonacci1(7), fibonacci2(7), fibonacci1(7))
# print(fibonacci2(15) == fibonacci1(15), fibonacci2(15), fibonacci1(15))

print(fibonacci2(4))

