import sys

input = sys.stdin.readline

# 접시 수, 초밥의 가짓수, 연속 접시 수, 쿠폰번호
N, d, k, c = map(int, input().split())
lst = [int(input().strip()) for _ in range(N)]
left, right = 0, 0
ans = 0

while left != N:
    right = left + k
    case = set()
    flag = True
    for i in range(left, right):
        i %= N
        case.add(lst[i])
        if lst[i] == c:
            flag = False

    cnt = len(case)
    if flag:
        cnt += 1
    ans = max(ans, cnt)
    left += 1

print(ans)
