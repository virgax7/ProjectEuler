# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

import mp.math_utils as mp
import numpy as np
ans = []
consec = 0
for i in range(2, 10000000000):
    tmp = mp.get_distinct_prime_facs(i)
    if len(tmp) == 4:
        ans.append(i)
    if len(tmp) == 4 and len(ans) > 3:
        if (np.array(ans)[-4:] - i == [-3,-2,-1,0]).all():
            ans = ans[len(ans) - 4]
            break

print(ans)
