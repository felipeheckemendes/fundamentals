def fibonacci1(n):
    """
    This implementation has fast time complexity, however its space complexity can be improved, since it stores all numbers up to the required.
    """
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
    """
    This implementation does not have space complexity, since it stores only the last 2 numbes on the sequence.
    However, it could be potentially be improved to be more succint.
    """
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

n = int(input())
print(fibonacci2(n))

