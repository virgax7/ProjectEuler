# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
import mp.math_utils as mp

ans = []

prime = 7
while len(ans) != 11:
    prime = mp.next_prime(prime)
    left = [int(str(prime)[:i+1]) for i in range(len(str(prime)))]
    right = [int(str(prime)[-(i+1):]) for i in reversed(range(len(str(prime))))]
    skip = False
    for l, r in zip(left, right):
        if mp.is_prime(l) is not True or mp.is_prime(r) is not True:
            skip = True
            break
    if skip:
        continue
    ans.append(prime)
print(sum(ans))
