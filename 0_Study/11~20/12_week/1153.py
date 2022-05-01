import sys

input = sys.stdin.readline

N, M = map(int, input().split())
book = list(map(int, input().split()))

plus, minus = [0,], [0,]
for b in book:
    if b > 0:
        plus.append(b)
    else:
        minus.append(abs(b))

plus.sort(reverse=True)
minus.sort(reverse=True)

ans = 0
for i in range(0, len(plus), M):
    ans += plus[i] * 2

for i in range(0, len(minus), M):
    ans += minus[i] * 2


ans -= max(plus[0], minus[0])
print(ans)
