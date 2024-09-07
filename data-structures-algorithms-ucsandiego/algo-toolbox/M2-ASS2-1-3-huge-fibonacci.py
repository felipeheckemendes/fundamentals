# Algorithm that returns the modulo m of the n-th fibonacci number

import time

def fibo_modulo(n, m):

    if n <= 1:
        return n
    n_minus_2, n_minus_1 = 0, 1

    for i in range (2, n+1):
        fibo_modulo = (n_minus_2 + n_minus_1) % m
        n_minus_2 = n_minus_1
        n_minus_1 = fibo_modulo
    return fibo_modulo


n, m = map(int, input().split())
# n = int(input())

# start_time = time.time()
print(fibo_modulo(n, m))
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Execution time: {elapsed_time:.6f} seconds")
