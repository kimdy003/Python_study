import sys

input = sys.stdin.readline

N, C = map(int, input().split())

wifi = list()
for _ in range(N):
    wifi.append(int(input()))

wifi.sort()

start = 1
end = wifi[-1] - wifi[0]

result = 0
while start <= end:
    mid = (start + end) // 2
    cnt, temp = 1, 0
    for i in range(1, len(wifi)):
        temp += wifi[i] - wifi[i - 1]
        if mid <= temp:
            cnt += 1
            temp = 0

    if cnt >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
