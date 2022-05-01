"""
2021.10.21
11505_구간 곱 구하기
"""
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
mul = [1]
for i in range(0, N):
    mul.append((mul[i] * lst[i]) % 1000000007)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:  # b번째 수를 c로 변경
        lst[b - 1] = c
        for i in range(b, N + 1):
            mul[i] = (mul[i - 1] * lst[i - 1]) % 1000000007

    if a == 2:  # b부터 c까지의 곱
        print(mul[c] // mul[b - 1])
