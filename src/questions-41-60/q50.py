# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import mp.math_utils as mp

limit = 1000000
primes = list(mp.prime_sieve(limit))

ans = 0
tot = 0
range_ij = 0
for i in range(len(primes)):
    sum = primes[i]
    for j in range(i + 1, len(primes)):
        sum += primes[j]
        if sum > limit:
            break
        if j - i > range_ij and sum in primes:
            range_ij = j - i
            ans = sum

print(ans)
