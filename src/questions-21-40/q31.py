#
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
from functools import reduce


nums = [1, 2, 5, 10, 20, 50, 100, 200]


def produce_combinations(given_coins, target_in_pence):
    def return_one_if_possible_path(idx, left_over):
        if left_over < 0 or idx >= len_given_coins:
            yield 0
        elif left_over == 0:
            yield 1
        else:
            yield from return_one_if_possible_path(idx, left_over - given_coins[idx])
            yield from return_one_if_possible_path(idx+1, left_over)

    given_coins.sort(reverse=True)
    len_given_coins = len(given_coins)
    return reduce(lambda x, y: x + y, return_one_if_possible_path(0, target_in_pence))


print(produce_combinations(nums, 200))

