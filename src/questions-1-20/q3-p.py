# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


# from what I read online, all ints > 1 is made up of a product of prime numbers
# that means you can just keep dividing from the smallest prime factor you can evenly divide by
# once you can't evenly divide by it, then try the next prime. You are guaranteed this because
# all ints > 1 is made up of a product of prime numbers and since there is that set of prime numbers
# whose product make up the number, using multiplication's commutative product, we should be guaranteed
# to found all the occurrences of that smallest prime factor(at the moment), since if it came later
# that means that it could have been found before, meaning it CAN'T come later
# for e.g. 24 is 2 * 2 * 2 * 3 and now the answer is the last factor, i.e. 3

import numpy
import mp.math_utils as m

number = 600851475143
divisor = 2

# https://stackoverflow.com/questions/5811151/why-do-we-check-up-to-the-square-root-of-a-prime-number-to-determine-if-it-is-pr
def next_prime(x):
    for i in range(x + 1, int(numpy.sqrt(number)) + 1):
        if m.is_prime(i):
            return i


while True:
    quotient = number / divisor
    if quotient - int(quotient) == 0:
        number = quotient
    else:
        divisor = next_prime(divisor)
    if m.is_prime(number):
        print(number)
        break




