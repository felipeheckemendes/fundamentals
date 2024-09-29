# Algorithm that returns the last digit of the n-th fibonacci number

def last_digit_fibo(n):

    if n <= 1:
        return n
    n_minus_2, n_minus_1 = 0, 1

    for i in range (2, n+1):
        last_digit_fibo = (n_minus_2 + n_minus_1) % 10
        n_minus_2 = n_minus_1
        n_minus_1 = last_digit_fibo
    return last_digit_fibo

n = int(input())
print(last_digit_fibo(n))