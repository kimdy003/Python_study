import sys

input = sys.stdin.readline

N, M = map(int, input().split())
train = [0] * N

for _ in range(M):
    op = list(map(int, input().split()))

    if op[0] == 1:
        i, x = op[1] - 1, op[2] - 1
        train[i] = train[i] | (1 << x)

    elif op[0] == 2:
        i, x = op[1] - 1, op[2] - 1
        train[i] = train[i] & ~(1 << x)

    elif op[0] == 3:
        i = op[1] - 1
        train[i] = train[i] << 1
        train[i] = train[i] & ~(1 << 20)

    else:
        i = op[1] - 1
        train[i] = train[i] >> 1

print(len(set(train)))
