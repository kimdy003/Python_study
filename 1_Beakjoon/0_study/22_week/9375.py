import sys

input = sys.stdin.readline

test = int(input())

for _ in range(test):
    N = int(input())
    dic = {}

    for _ in range(N):
        tmp = input().split()
        dic[tmp[1]] = dic.get(tmp[1], 0) + 1

    ans = 1
    for val in dic.values():
        ans *= val + 1

    print(ans - 1)
