import sys

input = sys.stdin.readline
calculation = lambda x, a: x // a + x % a

N = int(input())
for _ in range(N):
    l, r, a = map(int, input().split())
    ans = calculation(r, a)
    r = r // a * a - 1
    if r >= l:
        ans = max(ans, calculation(r, a))
    print(ans)
