#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# we are talking in the realm of integers

# lcm(a,b) = a * b  / gcd(a,b)
# a * b is a cm, but we need the lcm, so
# we divide by gcd(a,b) because if the number we divide the cm by isn't a shared factor of a and b
# it guarantees that the cm won't be evenly divided by both a and b
# note that if a number(y) is evenly divisible by another number(x), then y is evenly dividable
# by all factors x because you just need to amplify that factor of x by another number. What I'm getting
# at with this is that, if a number(y) is not evenly divisible by a factor of number(x), it's impossible
# for y to be evenly divisible by x, hence we need to find a common factor of a and b that the cm can be divided by
# and we need to find the greatest one to reduce cm to lcm

import math

lcm = 1
for i in range(1, 21):
    lcm = lcm * i // math.gcd(lcm, i)
print(lcm)

#1 2
#\/
#lcm  3
#  \ /
#  lcm
#
# the last lcm can be evenly divided by the previous lcm and the corresponding multiple(1 at the end and beginning) recursively
# this will make sense if you read the last paragraph
