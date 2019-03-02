# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
import functools
import math
from operator import mul


def get_curious_fractions():
    temps = [(num, denum)
            for num in range(1, 99)
                for denum in range(num+1, 100)
                    if (num % 10 == denum // 10
                        and denum % 10 != 0
                        and (num // 10) / (denum % 10) == num / denum)]
    nums, denums = zip(*temps)
    return nums, denums


nums, denums = get_curious_fractions()

numerators = functools.reduce(mul, nums)
denomenators = functools.reduce(mul, denums)

print(denomenators/math.gcd(numerators, denomenators))




