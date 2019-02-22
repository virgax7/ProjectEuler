#
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


nums = [1, 2, 5, 10, 20, 50, 100, 200]

ans = [0]
def combo_repeat(list, i, target, ans):
    if target == 0:
        ans[0] += 1
        return
    if target < 0:
        return
    for j in range(i, len(list)):
        combo_repeat(list, j, target - list[j], ans)


combo_repeat(nums, 0, 200, ans)
print(ans[0])

