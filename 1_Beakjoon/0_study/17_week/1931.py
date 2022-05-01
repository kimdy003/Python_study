import sys

input = sys.stdin.readline

N = int(input())
array = list(tuple(map(int, input().split())) for _ in range(N))

# array.sort(key=lambda x: x[0])
array.sort(key=lambda x: (x[1], x[0]))

ans, last = 0, 0
for start, end in array:
    if last <= start:
        last = end
        ans += 1

print(ans)
