# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position
# and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand
# common English words, how many are triangle words?

import urllib.request
import re
import string

data = urllib.request.urlopen("https://projecteuler.net/project/resources/p042_words.txt").read().decode()
words = [re.sub("\"", "", word).lower() for word in data.split(",")]
words = [sum([string.ascii_lowercase.index(c) + 1 for c in word]) for word in words]
limit = max(words)

from itertools import accumulate
triangle_nums = set(accumulate(range(1, limit + 1)))
print(sum(1 if word in triangle_nums else 0 for word in words))
