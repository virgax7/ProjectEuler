#
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
from functools import reduce

print(reduce(lambda x, y: (x + y ** y) % 10000000000, range(1, 1001)))
