"""
2021.10.21
16562_친구비
"""
import sys

input = sys.stdin.readline

N, M, Money = map(int, input().split())
friend_money = [0] + list(map(int, input().split()))
parent = [i for i in range(N + 1)]


def Find(parent, x):
    if parent[x] == x:
        return x

    parent[x] = Find(parent, parent[x])
    return parent[x]


def Union(parent, a, b):
    a = Find(parent, a)
    b = Find(parent, b)

    if friend_money[a] > friend_money[b]:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(M):
    a, b = map(int, input().split())
    Union(parent, a, b)

# 한번 더 진행하면서 묶어주기
for i in range(1, N + 1):
    parent[i] = Find(parent, i)


# 58% fail
set_parent = set(parent[1:])
ans = 0
for p in set_parent:
    ans += friend_money[p]

# AC
# visit = [0] * (N + 1)
# ans = 0
# for i in range(1, N + 1):
#     x = parent[i]
#     if visit[x] == 0:
#         visit[x] = 1
#         ans += friend_money[x]

print(ans if ans <= Money else "Oh no")
