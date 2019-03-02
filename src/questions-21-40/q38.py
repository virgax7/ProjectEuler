# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ... , n) where n > 1?
import itertools

ans = 0
number_with_nine_in_front = False
for i in range(9, int(987654322 / 2)):
    s = ""
    if i % 1000000 == 0:
        print(i)
    for j in itertools.count():
        s += str(i * (j + 1))
        if number_with_nine_in_front and s[0] != "9":
            break
        if len(s) > 9:
            break
        if ''.join(sorted(s)) == "123456789":
            if s[0] == "9":
                number_with_nine_in_front = True
            ans = max(int(s), ans)

print("the answer is ", ans)
