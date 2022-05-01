import sys

input = sys.stdin.readline

N = int(input())
line = [list(input().split()) for _ in range(N)]
order = sorted(sum(line, []))

queue = []
r, c = 0, 0
while order:
    if r == N and order:
        break
    if not queue:
        if order[0] == line[r][c]:
            del order[0]
        else:
            queue.append(line[r][c])
    else:
        if order[0] == line[r][c]:
            del order[0]
        elif order[0] == queue[-1]:
            del order[0]
            queue.pop()
            continue
        else:
            queue.append(line[r][c])

    c += 1
    if c == 5:
        c = 0
        r += 1
else:
    print("GOOD")
    exit(0)

print("BAD")
