import sys

input = sys.stdin.readline

test = int(input())

for _ in range(test):
    N = int(input())
    count, res = N // 3, N % 3
    ans = []

    for _ in range(count):
        if res == 1:
            ans.append("12")
        else:
            ans.append("21")

    if res > 0:
        ans.append(str(res))
    print(int("".join(ans)))
