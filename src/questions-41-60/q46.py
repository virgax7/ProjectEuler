# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import mp.math_utils as mp

for i in range(33, 1000000000000, 2):
    if mp.is_prime(i):
        continue
    primes = mp.prime_sieve(i)
    can_write = False
    for prime in primes:
        for j in range(i):
            j_ = prime + 2 * j ** 2
            can_write = j_ == i or can_write
            if j_ > i:
                break
        if can_write:
            break
    if not can_write:
        print(i)
        break
