#
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
import numpy as np

n = 1001
m = np.zeros((n, n))

num = n * n
i = -1
j = n
i_stride = n - 1
j_stride = n
while num > 0:
    i += 1
    j -= 1
    for k in range(j_stride):
        m[i, j - k] = num
        num -= 1
    for k in range(i_stride):
        m[i + 1 + k, i] = num
        num -= 1
    j_stride -= 1
    for k in range(j_stride):
        m[j, i + 1 + k] = num
        num -= 1
    i_stride -= 1
    for k in range(i_stride):
        m[j - k - 1, j] = num
        num -= 1
    i_stride -= 1
    j_stride -= 1
left_diag = np.diag(m)
right_diag = np.diag(np.fliplr(m))
print(np.sum(left_diag) + np.sum(right_diag) - 1)
