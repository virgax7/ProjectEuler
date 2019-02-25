#
#
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)
import numpy as np

print(sum([i if str(np.binary_repr(i)) == str(np.binary_repr(i))[::-1] and str(i)[::-1] == str(i) else 0 for i in range(1000000)]))
