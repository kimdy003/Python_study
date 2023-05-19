import sys

input = sys.stdin.readline


def calc(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


if __name__ == "__main__":
    N = int(input())
    building = list(map(int, input().split()))
    answer = 0

    for idx, b in enumerate(building):
        viewMax = 0
        leftMax = int(1e9)  # 왼쪽의 기울기 최솟값
        rightMax = -int(1e9)  # 오른쪽의 기울기 최댓값

        for i in range(idx - 1, -1, -1):  # 왼쪽
            c = calc(idx + 1, b, i + 1, building[i])
            if c < leftMax:
                leftMax = c
                viewMax += 1

        for i in range(idx + 1, N):
            c = calc(idx + 1, b, i + 1, building[i])
            if c > rightMax:
                rightMax = c
                viewMax += 1

        answer = max(answer, viewMax)
    print(answer)
