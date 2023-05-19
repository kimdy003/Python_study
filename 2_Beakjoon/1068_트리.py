import sys

input = sys.stdin.readline


def dfs(num, lst):
    lst[num] = -2
    for i in range(len(lst)):
        if num == lst[i]:
            dfs(i, lst)


n = int(input())
lst = list(map(int, input().split()))
remove = int(input())
count = 0

dfs(remove, lst)
count = 0
for i in range(len(lst)):
    if lst[i] != -2 and i not in lst:
        count += 1
print(count)
