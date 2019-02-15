#
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?

import numpy as np
memo = {}
k = 21
spots = np.ones((k,k))

def solve(spots, i, j):
    sum = 0
    if i == k - 1 and j == k - 1:
        return 1
    if i < k - 1:
        if (i + 1,j) in memo:
            sum += memo[(i+1, j)]
        else:
            sum += solve(spots, i + 1, j)
    if j < k - 1:
        if (i,j + 1) in memo:
            sum += memo[(i,j + 1)]
        else:
            sum += solve(spots, i, j + 1)
    memo[(i,j)] = sum
    return sum

print(solve(spots, 0, 0))

