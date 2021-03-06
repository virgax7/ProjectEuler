# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
from functools import reduce

prev = 89
cur = 144
i = 12

while True:
    tmp = prev + cur
    prev = cur
    cur = tmp
    i += 1
    if len(str(cur)) >= 1000:
        print(i)
        break

# One-liner fibonacci for a record
def fib(n):
    return reduce(lambda item, _: (item[1], item[0] + item[1]), range(n-1), (1, 1))[0]

here = fib(i)
assert here == cur, '{}'.format(here/cur)

