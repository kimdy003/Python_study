import sys

input = sys.stdin.readline


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


if __name__ == "__main__":
    N, M = map(int, input().split())
    print(gcd(N, M))
