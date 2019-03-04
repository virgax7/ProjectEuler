# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?
import mp.math_utils as mp
import itertools
from operator import itemgetter

prime_set = list(map(lambda x : (''.join(sorted(str(x))),x), (filter(lambda x : len(str(x)) > 3, mp.prime_sieve(10000)))))
prime_set.sort()
prime_set = [(g[0], [num[1] for num in g[1]]) for g in itertools.groupby(prime_set, itemgetter(0))]
prime_set = list(filter(lambda g: len(g[1]) > 3, prime_set))
prime_set = list(filter(lambda g: any([g[1][i+2] - g[1][i+1] == 3330 and g[1][i+1] - g[1][i] == 3330 for i in range(0, len(g[1]) - 2)]), prime_set))
print(list(map(itemgetter(1), prime_set)))
