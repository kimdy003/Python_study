import sys

input = sys.stdin.readline
INF = int(1e9)

if __name__ == "__main__":
    C, N = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    minCost = [0] + [INF] * (C + 100)

    for cost, customer in lst:
        for i in range(customer, C + 100):
            minCost[i] = min(minCost[i - customer] + cost, minCost[i])

    print(min(minCost[C : C + 101]))
