#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

ans_set = set()
stop = int(''.join(map(str, [9] * 7)))
for i in range(stop):
    for j in range(stop):
        prod = str(i * j)
        s = prod + str(i) + str(j)
        if len(s) > 9:
            break
        if ''.join(sorted(s)) == '123456789':
            ans_set.add(int(prod))

print(sum(ans_set))

