import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
sum_lst = [lst[0]]

for num in lst[1:]:
    sum_lst.append(sum_lst[-1] + num)

for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        print(sum_lst[b - 1])
    else:
        print(sum_lst[b - 1] - sum_lst[a - 2])
