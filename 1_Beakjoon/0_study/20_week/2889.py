import sys

input = sys.stdin.readline

N = int(input())
_input = list(input().split())

ans = []
for num in _input:
    temp = int(num, 16)
    if 64 <= temp <= 95:
        ans.append("-")
    else:
        ans.append(".")

print("".join(ans))
