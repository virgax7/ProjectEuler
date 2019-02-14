# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

mem = {}
ans = 0
def cf(i):
    terms = 1
    if i == 13:
        print()
    while True:
        if i == 1:
            break
        if i in mem:
            return terms + mem[i]
        if i % 2 == 0:
            i /= 2
        else:
            i = 3 * i + 1
        terms += 1
    return terms

max_terms = 0
for i in range(1, 1000000):
    terms = cf(i)
    mem[i] = terms
    if max_terms < terms:
        ans = i
    max_terms = max_terms if max_terms > terms else terms

print(ans)

