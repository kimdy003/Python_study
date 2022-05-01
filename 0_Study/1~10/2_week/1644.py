import sys

input = sys.stdin.readline
N = int(input())


def Prime_list(N):
    temp = [False, False] + [True] * (N - 1)
    M = int(N ** 0.5)

    for i in range(2, M + 1):
        if temp[i]:
            for j in range(i * 2, N + 1, i):
                temp[j] = False

    return [i for i in range(2, N + 1) if temp[i]]


prime = Prime_list(N)

left, right = 0, 0
Sum, cnt = 0, 0  # N=1인 경우 생각 'Sum = prime[left]' -> 'Sum = 0'
while True:
    if N <= Sum:
        if Sum == N:
            cnt += 1
        Sum -= prime[left]
        left += 1
    elif right == len(prime):
        break
    else:
        Sum += prime[right]
        right += 1

print(cnt)
