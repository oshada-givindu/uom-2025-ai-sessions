#problem 10: Summation of primes
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def sum_of_primes(limit):
    return sum(i for i in range(2, limit) if is_prime(i))
print(sum_of_primes(2000000))

