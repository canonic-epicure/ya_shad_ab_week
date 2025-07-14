from itertools import chain
import sys
import re

str = sys.stdin.read()

numbers = re.findall(r"\d+", str)

for i in chain({}.items()):
    pass

print(int(numbers[0]) + int(numbers[1]))