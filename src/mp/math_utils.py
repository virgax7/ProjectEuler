import numpy as np

def is_prime(x):
    for i in range(2, int(np.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

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
