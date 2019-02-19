# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math

def get_prop_div_sum(x):
    div_sum = 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if i * i == x:
                div_sum += x / i
            else:
                div_sum += i + x / i
    return div_sum + 1

ab_numbers = set()
for i in range(12, 28124):
    div_sum = get_prop_div_sum(i)
    if div_sum > i:
        ab_numbers.add(i)
ans = 0
cannot_be_two_ab_num = [i for i in range(1,24)]
sorted(ab_numbers)
for i in range(24, 28124):
    can_add = False
    for j,data in enumerate(ab_numbers):
        if data * 2 > i:
            break
        if i - data in ab_numbers:
            can_add = True
            break
    if can_add:
        continue
    cannot_be_two_ab_num.append(i)

print(sum((cannot_be_two_ab_num)))
#

