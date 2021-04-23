#
#  1759.py
#  암호 만들기
#
#  Create by 김도영 on 2021/04/22
#

from sys import stdin
from itertools import combinations

l, c= map(int, stdin.readline().split())
alpha = sorted(stdin.readline().split())
print(alpha)
lst = set('aeiou')

com = list(combinations(alpha, l))

for i in com:
    c = set(i) - lst
    if 2 <= len(c) and l - len(c) >= 1:
        print(''.join(i))



