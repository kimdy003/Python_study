import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    cranes = sorted(list(map(int, input().split())), reverse=True)

    M = int(input())
    boxs = sorted(list(map(int, input().split())), reverse=True)

    if boxs[0] > cranes[0]:
        print(-1)
        exit(0)

    time = 0
    while boxs:
        for crane in cranes:
            for box in boxs:
                if crane >= box:
                    boxs.remove(box)
                    break

        time += 1
    print(time)
