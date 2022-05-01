import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    _input = list(input().strip())
    string = input().strip()
    for i, a in enumerate(_input):
        if a == string:
            left, right = i, len(_input) - i - 1
            if left % 2 == 0 and right % 2 == 0:
                print("YES")
                break
    else:
        print("NO")
