from num2words import num2words
import re

ans = 0
for i in range(1, 1001):
    num = num2words(i)
    ans += len(re.sub(r"-| ", "", num))
print(ans)
