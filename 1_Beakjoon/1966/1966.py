from sys import stdin

T = int(stdin.readline().strip())

while T>0:
    T -= 1

    n, m = map(int, stdin.readline().split())
    queue = list(map(int, stdin.readline().split()))
    idx = list(range(len(queue)))
    idx[m] = "target"

    ans = 0
    while True:
        if queue[0] == max(queue):
            ans += 1

            if idx[0] == "target":
                print(ans)
                break
            else:
                queue.pop(0)
                idx.pop(0)
        
        else:
            queue.append(queue.pop(0))
            idx.append(idx.pop(0))
        
