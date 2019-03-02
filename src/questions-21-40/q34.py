#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math
import itertools

limit = 0
for i in itertools.count():
    limit = i
    digit_len = len(str(i))
    if i > sum([math.factorial(9)] * digit_len):
        break


ans = 0
for i in range(3, limit):
    if sum([math.factorial(int(num)) for num in list(str(i))]) == i:
        ans += i

print(ans)

