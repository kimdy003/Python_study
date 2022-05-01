import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    people = [tuple(map(int, input().split())) for _ in range(N)]
    people.sort()
    Max = people[0][1]
    cnt = 1

    for _, score in people[1:]:
        if Max > score:
            cnt += 1
            Max = score
    print(cnt)
