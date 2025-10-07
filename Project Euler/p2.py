#problem 02: Even Fibonacci numbers
def sum_of_even_fibonacci(limit):
    a, b = 0, 1
    total = 0
    while b < limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total
print(sum_of_even_fibonacci(4000000))

