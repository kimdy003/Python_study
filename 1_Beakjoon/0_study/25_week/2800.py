import sys
from itertools import combinations

input = sys.stdin.readline

_input = list(input().strip())

stack, pos = [], []
ans = set()

for i, k in enumerate(_input):
    if k == "(":
        stack.append(i)
    elif k == ")":
        pos.append((stack.pop(), i))

for i in range(1, len(pos) + 1):
    combin = combinations(pos, i)
    for c in combin:
        temp = _input[:]

        for s, e in c:
            temp[s], temp[e] = "", ""
        ans.add("".join(temp))

for i in sorted(list(ans)):
    print(i)

# print(*ans, sep='\n')
