# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import mp.math_utils as m
pm = 2
for i in range(10000):
    pm = m.next_prime(pm)
print(pm)
