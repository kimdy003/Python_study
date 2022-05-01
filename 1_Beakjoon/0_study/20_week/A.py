import sys

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):
    N, S = map(int, input().split())
    print(S // N ** 2)
