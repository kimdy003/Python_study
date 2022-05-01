import sys


import sys

input = sys.stdin.readline

lst = list(input().strip())
p = list(input().strip())

dic = {}
for i, d in enumerate(lst):
    dic[d] = dic.get(d, []) + [i]

if p[0] not in dic:
    print(0)
    exit()

for start in dic[p[0]]:
    end = start + len(p)
    if lst[start:end] == p:
        print(1)
        break
else:
    print(0)
