import numpy as np
from functools import reduce

def is_prime(x):
    for i in range(2, int(np.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return x > 1

def next_prime(x):
    while True:
        x += 1
        if is_prime(x):
            return x

def prime_sieve(limit):
    prime = [True] * limit
    prime[0] = prime[1] = False

    for p, is_prime in enumerate(prime):
        if is_prime:
            yield p
            for n in range(p * p, limit, p):
                prime[n] = False

def get_distinct_prime_facs(num):
    assert num > 1
    divisor = 2
    result = set()
    while True:
        quotient = num / divisor
        if quotient - int(quotient) == 0:
            result.add(divisor)
            num = quotient
        else:
            divisor = next_prime(divisor)
        if num == 1 or is_prime(num):
            result.add(num)
            if 1 in result:
                result.remove(1)
            return result

# One-liner fibonacci for a record
def fib(n):
    return reduce(lambda item, _: (item[1], item[0] + item[1]), range(n), (0, 1))[1]
