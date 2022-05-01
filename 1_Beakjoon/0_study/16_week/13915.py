import sys

input = sys.stdin.readline

while True:
    try:
        N = int(input())
        lst = set()
        for _ in range(N):
            temp = set(map(int, input().strip()))
            lst.add("".join([str(t) for t in temp]))

        print(len(lst))

    except:
        break
