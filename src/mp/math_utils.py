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
