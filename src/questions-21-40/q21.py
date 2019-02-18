# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
import math

def get_prop_div_sum(x):
    div_sum = 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            div_sum += i + x / i
    return div_sum + 1

ans = 0
for i in range(1, 10000):
    prop_div_sum = get_prop_div_sum(i)
    if prop_div_sum < 10000 and prop_div_sum != i:
        other_prop_div_sum = get_prop_div_sum(prop_div_sum)
        if i == other_prop_div_sum:
            ans += i

print(ans)
