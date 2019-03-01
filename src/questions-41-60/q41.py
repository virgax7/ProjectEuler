# We shall say that an n-digit number is pandigital if it
# makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

import mp.math_utils as mp

sieve = mp.prime_sieve(987654322)

s = "123456789"
ans = 0
for prime in sieve:
    if ''.join(sorted(str(prime))) == s[0:len(str(prime))]:
        ans = max(ans, prime)
print(ans)
