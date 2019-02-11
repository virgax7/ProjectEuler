import mp.math_utils as m

sum = 0
for i in range(2, 2000000):
    if m.is_prime(i):
        sum += i
print(sum)
