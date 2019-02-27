#
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

ans_set = {i: 0 for i in range(1, 1001)}

for p in range(120, 1001):
    for i in range(1, p):
        for j in range(i, p - i):
            k = p - j - i
            if i ** 2 + j ** 2 == k ** 2:
                ans_set[p] += 1

print(max(ans_set.keys(), key=lambda x: ans_set[x]))
