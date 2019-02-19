# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

import urllib.request
import re
from string import ascii_lowercase

data = urllib.request.urlopen("https://projecteuler.net/project/resources/p022_names.txt").read().decode()
names = [re.sub("\"", "", name) for i,name in enumerate(data.split(","))]
names.sort()
names = sum([(i+1) * sum(list(map(lambda c: ascii_lowercase.index(c) + 1, list(name.lower())))) for i,name in enumerate(names)])
print(names)

