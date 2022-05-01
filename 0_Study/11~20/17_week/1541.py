import sys

input = sys.stdin.readline

arr = input().strip().split("-")
stack = []

for a in arr:
    _sum = 0
    for num in a.split("+"):
        _sum += int(num)
    stack.append(_sum)

ans = stack[0]
for num in stack[1:]:
    ans -= num
print(ans)
